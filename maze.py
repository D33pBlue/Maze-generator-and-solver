# A maze is a square of r*c cells, each of them consists in a dictionary
# with the following keys:
# -r: the row in the square
# -c: the column in the square
# -n: True if and only if there is a wall at north of the cell
# -s: True if and only if there is a wall at south of the cell
# -e: True if and only if there is a wall at east of the cell
# -w: True if and only if there is a wall at west of the cell
# -state: a string with the state of the cell
# -adj: the adjacency list of the cell

import random

def make_cell(r,c,n=True,s=True,e=True,w=True,state=""):
	cell=dict()
	cell['r']=r
	cell['c']=c
	cell['n']=n
	cell['s']=s
	cell['e']=e
	cell['w']=w
	cell['state']=state
	cell['adj']=[]
	return cell

def add_adj(cell,adj):
	if not adj in cell['adj']:
		cell['adj'].append(adj)

def get_shape(L):
	return (len(L),len(L[0]))

# L is a array of cells (square)
def check_cell(L,c):
	Lr,Lc = get_shape(L)
	i,j=c
	if i<0 or i>=Lr or j<0 or j>=Lc:
		return False
	return L[i][j] != None


def adjacent(c1,c2):
	if abs(c1[0]-c2[0]) ==1 and c1[1] == c2[1]:
		return True
	if abs(c1[1]-c2[1]) ==1 and c1[0] == c2[0]:
		return True
	return False


def has_cycle(L,end):
	for r in L:
		for v in r:
			v['visited']=False
	for r in L:
		for v in r:
			if not v['visited']:
				stack=[]
				state=(None,v)
				stack.append(state)
				while len(stack)>0:
					prec,c = stack.pop()
					if c['visited']:
						end[0] = c
						return True
					c['visited']=True
					for k in c['adj']:
						if k != prec:
							state=(c,k)
							stack.append(state)
	return False

def find_cycle(start):
	if start == None:
		return []
	stack = []
	for c in start['adj']:
		stack.append((c,[start]))
	while len(stack)>0:
		c,path = stack.pop()
		path.append(c)
		if c == start:
			return path
		for cell in c['adj']:
			if not cell in path or (cell==start and cell!=path[len(path)-1]):
				stack.append((cell,path[:]))
	return []

def find_path(c1,c2):
	stack = []
	stack.append((c1,[]))
	while len(stack)>0:
		c,path = stack.pop()
		path.append(c)
		if c == c2:
			return path
		for cell in c['adj']:
			if not cell in path:
				stack.append((cell,path[:]))
	return []



def findable_cells(c):
	stack=[]
	visited=set()
	stack.append(c)
	while len(stack)> 0:
		c_corr=stack.pop()
		coord=(c_corr['r'],c_corr['c'])
		visited.add(coord)
		for k in c_corr['adj']:
			k_c = (k['r'],k['c'])
			if not k_c in visited:
				stack.append(k)
	return len(visited)


def connected(L):
	r,c=get_shape(L)
	return r*c==findable_cells(L[0][0])


def delete_random_wall(L,cell):
	# print cell
	i,j=cell['r'],cell['c']
	k=(i,j)
	k_n=(i-1,j)
	k_s=(i+1,j)
	k_e=(i,j+1)
	k_w=(i,j-1)
	possible_neighbours=[]
	if check_cell(L,k_n):
		possible_neighbours.append(k_n)
	if check_cell(L,k_s):
		possible_neighbours.append(k_s)
	if check_cell(L,k_e):
		possible_neighbours.append(k_e)
	if check_cell(L,k_w):
		possible_neighbours.append(k_w)
	if len(possible_neighbours)>0:
		random.shuffle(possible_neighbours)
		choosen = possible_neighbours.pop()
		ic,jc=choosen
		neigh=L[ic][jc]
		add_adj(neigh,cell)
		add_adj(cell,neigh)
		if ic<i:
			cell['n']=False
			neigh['s']=False
		elif ic>i:
			cell['s']=False
			neigh['n']=False
		elif jc<j:
			cell['w']=False
			neigh['e']=False
		elif jc>j:
			cell['e']=False
			neigh['w']=False
	# print cell


def low_degree_cells(L):
	m=4
	for r in L:
		for c in r:
			if len(c['adj'])<m:
				m=len(c['adj'])
			if m==0:
				break
	cells=[]
	for r in L:
		for c in r:
			if len(c['adj'])==m:
				cells.append(c)
	return cells


def put_wall(c1,c2):
	c1['adj'].remove(c2)
	c2['adj'].remove(c1)
	i,j=c1['r'],c1['c']
	ic,jc=c2['r'],c2['c']
	if ic<i:
		c1['n']=True
		c2['s']=True
	elif ic>i:
		c1['s']=True
		c2['n']=True
	elif jc<j:
		c1['w']=True
		c2['e']=True
	elif jc>j:
		c1['e']=True
		c2['w']=True


# def importa(file):
# 	contenuto = []
# 	#viene letto il contenuto del file in una lista di string
# 	f = open(file)
# 	if f==None:
# 		print "Errore nella lettura del file"
# 		return None
# 	for r in f.readlines():
# 		contenuto.append(r.strip("\n"))
# 	f.close()
# 	text_r = len(contenuto)
# 	if text_r == 0:
# 		return None
# 	text_c = 0
# 	for r in contenuto:
# 		if len(r)>text_c:
# 			text_c=len(r)
# 	#verifica della conformita' del contenuto del file
# 	for r_i in contenuto:
# 		if len(r_i) != text_c or contiene_caratteri_non_conformi(r_i):
# 			print "Errore nel formato del file"
# 			return None
# 	r=(text_r-1)/2
# 	c=(text_c-1)/2
# 	#inizializzazione della matrice che rappresenta il maze
# 	maze = []
# 	for i in range(r):
# 		maze.append([])
# 		for j in range(c):
# 			maze[i].append(None)
# 	#costruzione della matrice inserendo le Celle in base ai dati del file
# 	for i in range(r):
# 		for j in range(c):
# 			#coordinate della cella nel testo
# 			t_i=1+2*i
# 			t_j=1+2*j
# 			#costruzione della cella
# 			maze[i][j]=crea_cella(
# 				r = i,
# 				c = j,
# 				n = contenuto[t_i-1][t_j]=='*',
#  				s = contenuto[t_i+1][t_j]=='*',
#  				o = contenuto[t_i][t_j-1]=='*',
#  				e = contenuto[t_i][t_j+1]=='*',
# 	 			stato = ""
# 			)
# 			#aggiornamento delle celle collegate (adiacenti e non separate da muro)
# 			possibili_collegate=[(i-1,j),(i,j-1)]
# 			for p_col in possibili_collegate:
# 				if(cella_presente(maze,p_col) and
# 					collegate(maze,(i,j),p_col)):
# 					cella_col=maze[p_col[0]][p_col[1]]
# 					add_collegata(maze[i][j],cella_col)
# 					add_collegata(cella_col,maze[i][j])
# 	return maze


def exits(L):
	u = []
	r,c= get_shape(L)
	for j in range(c):
		if L[0][j]['n'] == False:
			if not (0,j) in u:
				u.append((0,j))
		if L[r-1][j]['s'] == False:
			if not (r-1,j) in u:
				u.append((r-1,j))
	for i in range(r):
		if L[i][0]['w'] == False:
			if not (i,0) in u:
				u.append((i,0))
		if L[i][c-1]['e'] == False:
			if not (i,c-1) in u:
				u.append((i,c-1))
	return u


def add_exit(L):
	r,c= get_shape(L)
	possible_exits=[]
	for j in range(c):
		possible_exits.append((0,j))
		possible_exits.append((r-1,j))
	for i in range(r):
		possible_exits.append((i,0))
		possible_exits.append((i,c-1))
	random.shuffle(possible_exits)
	u=None
	while len(possible_exits)>0 and u==None:
		u1=possible_exits.pop()
		if not u1 in exits(L):
			u=u1
	if u != None:
		ui,uj=u
		if ui==0:
			L[ui][uj]['n']=False
		elif ui==r-1:
			L[ui][uj]['s']=False
		elif uj==0:
			L[ui][uj]['w']=False
		elif uj==c-1:
			L[ui][uj]['e']=False


def show(L):
	r,c = get_shape(L)
	line=""
	for i in range(r):
		for j in range(c):
			if L[i][j]['n']:
				line+="+---"
			else:
				line+="+   "
		line+= "+"
		print line
		line = ""
		for j in range(c):
			if L[i][j]['w']:
				if L[i][j]['state'] == 'Path':
					line+="| X "
				else:
					line+="|   "
			else:
				if L[i][j]['state'] == 'Path':
					line+="  X "
				else:
					line+="    "
		if L[i][c-1]['e']:
			line+= "|"
		print line
		line=""
	for j in range(c):
		if L[i][j]['s']:
			line+="+---"
		else:
			line+="+   "
	line+="+"
	print line



def perfect(L):
	if L is None:
		return False
	if has_cycle(L,[None]):
		return False
	return connected(L)


def make_maze(r,c):
	L = [[make_cell(i,j) for j in range(c)] for i in range(r)]
	for l in L:
		for cell in l:
			delete_random_wall(L,cell)
	while not perfect(L):
		cycle=[]
		end = [None]
		while has_cycle(L,end):
			cycle = find_cycle(end[0])
			c1=cycle.pop()
			c2=cycle.pop()
			put_wall(c1,c2)
			end = [None]
		while not connected(L):
			for k in low_degree_cells(L):
				delete_random_wall(L,k)
			while has_cycle(L,end):
				cycle = find_cycle(end[0])
				c1=cycle.pop()
				c2=cycle.pop()
				put_wall(c1,c2)
				end = [None]
	add_exit(L)
	add_exit(L)
	return L

if __name__ == '__main__':
	L = make_maze(14,14)
	show(L)
