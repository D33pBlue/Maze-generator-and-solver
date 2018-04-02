import random


# Per rappresentare le caselle del labirinto (che per definizione e'
# una scacchiera rettangolare di rxc quadrati) si sono utilizzati dei
# dizionari con le seguenti chiavi:
# -r: indica la riga della scacchiera del labirinto in cui si trova
# -c: indica la colonna della scacchiera del labirinto in cui si trova
# -n: True se e' presente un muro a nord della Cella, False altrimenti
# -s: True se e' presente un muro a sud della Cella, False altrimenti
# -e: True se e' presente un muro a est della Cella, False altrimenti
# -o: True se e' presente un muro a ovest della Cella, False altrimenti
# -stato: e' una string che contiene lo stato della Cella
# -collegate: e' l'insieme delle Celle adiacenti alla Cella che sono
# 		raggiungibili (non sono separate da muri)
#
# Un labirinto (maze) sara' una matrice (lista di liste) di celle, che saranno
# quindi dizionari.


# -Parametri: le coordinate r e c della cella nel labirinto, un valore booleano
#  che indica la presenza di muro per ogni lato della cella e lo stato della cella
# -Funzionamento: istanzia e ritorna una cella (che e' un dizionario) assegnando
#  ai campi dati i valori passati per parametro
# -Valore di ritorno: un dizionario che rappresenta una cella
def crea_cella(r,c,n=True,s=True,e=True,o=True,stato=""):
	cella=dict()
	cella['r']=r
	cella['c']=c
	cella['n']=n
	cella['s']=s
	cella['e']=e
	cella['o']=o
	cella['stato']=stato
	cella['collegate']=[]
	return cella



# -Parametri: due celle (dizionari)
# -Funzionamento: aggiunge alla lista delle celle collegate alla prima cella
# (adiacenti non separate da muro) la seconda cella, se non e' gia presente
# -Valore di ritorno: None
def add_collegata(cella,collegata):
	if not collegata in cella['collegate']:
		cella['collegate'].append(collegata)



# -Parametri: una stringa che rappresenta una riga del labirinto in formato testuale
# -Funzionamento: verifica se nella stringa siano presenti caratteri non
#  conformi allo standard di rappresentazione testuale del labirinto, ossia
#  caratteri diversi da " " o "*"
# -Valore di ritorno: True se nella stringa sono presenti caratteri non
#  conformi, False altrimenti
def contiene_caratteri_non_conformi(riga):
	for e in riga:
		if e != ' ' and e != '*':
			return True
	return False



# -Parametri: un labirinto (maze) ben formato L e una tuple c di interi che rappresenta
#  possibili coordinate di una cella
# -Funzionamento: verifica che esista una cella e sia ben definita alle coordinate
#  specificate dalla tuple
# -Valore di ritorno: True se la cella esiste e non e' None, False altrimenti
def cella_presente(L,c):
	#ottengo le righe e le colonne in L
	Lr,Lc = righe_colonne(L)
	i,j=c
	#se le coordinate non sono compatibili con la dimensione di L ritorno False
	if i<0 or i>=Lr or j<0 or j>=Lc:
		return False
	#se la Cella esiste verifico non sia None
	return L[i][j] != None



# -Parametri: due tuple di interi che rappresentano coordinate
# -Funzionamento: verifica se le due coordinate identificano punti adiacenti
# -Valore di ritorno: True se sono adiacenti, False altrimenti
def adiacenti(c1,c2):
	if abs(c1[0]-c2[0]) ==1 and c1[1] == c2[1]:
		return True
	if abs(c1[1]-c2[1]) ==1 and c1[0] == c2[0]:
		return True
	return False



# -Parametri: una cella (la cella corrente), una seconda cella
#  (che puo' essere None) che rappresenta la cella del passo precedente e una
#  lista che contiene le celle visitate dalla funzione
# -Funzionamento: a partire dalla cella fornita, esplora ricorsivamente il grafo
#  connesso alla stessa, visitando le celle presenti nell'insieme cella[collegate]
#  e inserendole nella lista percorso. Se ritorna in una cella visitata in
#  precedenza la funzione restituisce True per segnalare la presenza di un ciclo,
#  altrimenti restituisce False una volta esplorato tutto il grafo
# -Valore di ritorno: True se nell'esplorare il grafo ritorna su celle visitate
#  in precedenza (il grafo contiene un ciclo), False altrimenti. Effettua
#  inoltre side effect sulla lista percorso, inserendovi il cammino intrapreso
def visita_grafo(cella,prec,percorso):
        percorso.append(cella)
        cella['visitato']=True
        for c in cella['collegate']:
        	#non considera la cella prec (visitata al passo precedente)
        	#e verifica se le altre sono gia' state inserite in percorso
        	#o se e' gia' stato trovato un ciclo
            if (c != prec and (c in percorso or visita_grafo(c,cella,percorso))):
                return True
        percorso.remove(cella)
        return False



# -Parametri: una lista di liste di celle L che rappresenta un labirinto (maze)
#  e una lista vuota
# -Funzionamento: verifica se in L (visto come grafo) e' presente un ciclo
#  invocando la funzione visita_grafo su ogni nodo (a priori non e' detto che
#  il grafo sia connesso)
# -Valore di ritorno: True se e' presente un ciclo, False altrimenti. Se il ciclo
#  e' presente allora la lista percorso contiene le celle del cammino effettuato
def trova_ciclo(L,percorso):
	for r in L:
		for v in r:
			v['visitato']=False
	for r in L:
		for v in r:
			if not v['visitato']:
				if visita_grafo(v,None,percorso):
					return True
	return False

def contiene_ciclo(L):
	for r in L:
		for v in r:
			v['visitato']=False
	for r in L:
		for v in r:
			if not v['visitato']:
				stack=[]
				stato=(None,v)
				stack.append(stato)
				while len(stack)>0:
					prec,c = stack[len(stack)-1]
					del stack[len(stack)-1]
					if c['visitato']:
						return True
					c['visitato']=True
					for k in c['collegate']:
						if k != prec:
							stato=(c,k)
							stack.append(stato)
	return False


# -Parametri: due celle c1 e c2 del labirinto (maze) e una lista vuota
#  dove verra' memorizzato il cammino se esiste
# -Funzionamento: esplora ricorsivamente il grafo connesso a c1 (utilizzando
#  l'insieme di celle collegate per determinare i percorsi possibili) fino
#  a che raggiunge c2 o non si ha la possibilita' di procedere su nuove celle
#  che non siano gia' state viste in precedenza. Memorizza il cammino fatto
#  nella lista percorso. Se la cella c1 appartiene ad in labirinto perfetto
#  il cammino esiste ed e' unico
# -Valore di ritorno: True se esiste un cammino dalla Cella c1 alla Cella c2
#  nel labirinto (maze) cui appartengono, False altrimenti. Nel caso ci sia
#  il cammino questo viene memorizzato nella lista percorso
def esiste_cammino(c1,c2,percorso):
	percorso.append(c1)
	#se c2 viene raggiunta esiste cammino
	if c1 == c2:
		return True
	#se tutti i possibili spostamenti di un ramo sono gia' stati analizzati
	#e non si e' in c2, non si e' trovato il cammino
	visitato_interamente=True
	for cella in c1['collegate']:
		if not cella in percorso:
			visitato_interamente=False
	if visitato_interamente:
		percorso.remove(c1)
		return False
	#tutte le possibili mosse vengono analizzate fino a che non viene trovato
	#un cammino o non si e' visitato tutto il grafo
	scelte=[]
	for s in c1['collegate']:
		if not s in percorso:
			scelte.append(s)
	for scelta in scelte:
		if esiste_cammino(scelta,c2,percorso):
			return True
	#se si e' visitato tutto il grafo visitabile a partire da c1
	#e non si e' trovato un cammino verso c2, questo non esiste
	percorso.remove(c1)
	return False



# -Parametri: due celle di un labirinto (maze) che non presenti cicli, quella da cui
#  partire e quella precedente (None alla prima invocazione)
# -Funzionamento: visita ricorsivamente le celle raggiungibili a partire da c
#  (senza tornare indietro) e conta quante sono. Per la convergenza della funzione
#  e' importante che il grafo non presenti cicli
# -Valore di ritorno: il numero di celle per cui esiste un cammino da c per raggiungerle
def celle_visitabili(c):
	stack=[]
	visitate=set()
	stack.append(c)
	while len(stack)> 0:
		c_corr=stack[len(stack)-1]
		del stack[len(stack)-1]
		#print c_corr
		coord=(c_corr['r'],c_corr['c'])
		visitate.add(coord)
		for k in c_corr['collegate']:
			k_c = (k['r'],k['c'])
			if not k_c in visitate:
				stack.append(k)
	return len(visitate)


# -Parametri: un labirinto (maze) ben formato
# -Funzionamento: verifica che il labirinto sia connesso confrontando il numero
#  di celle totale con il numero di celle connesse alla cella (0,0), ottenuto
#  tramite la funzione celle_visitabili. Se il numero di celle connesse a (0,0)
#  e' pari al numero totale di celle significa che dalla cella (0,0) sono
#  raggiungibili tutte le altre (e vice versa), pertanto il grafo risulta connesso
# -Valore di ritorno: True se il labirinto e' connesso, False altrimenti
def connesso(L):
	r,c=righe_colonne(L)
	return r*c==celle_visitabili(L[0][0])



# -Parametri: un labirinto (maze) ben formato, una cella del labirinto e una lista
# -Funzionamento: a partire dalla cella fornita esplora alla cieca il labirinto,
#  modificando lo stato delle celle percorse e inserendo l'elenco delle stesse
#  nella lista cammini
# -Valore di ritorno: True se esiste cammino dalla cella cella ad una uscita del
#  labirinto, False altrimenti. Se esiste salva il cammino nella lista cammini
def uscita_pesente(L,cella,cammini):
	i=cella['r']
	j=cella['c']
	k=(i,j)
	k_n=(i-1,j)
	k_s=(i+1,j)
	k_e=(i,j+1)
	k_o=(i,j-1)
	set_stato(L,k,"Percorso")
	cammini.append(k)
	if k in uscite(L):
		return True
	if( (cella['n'] or get_stato(L,k_n)=="Percorso")
		and (cella['s'] or get_stato(L,k_s)=="Percorso")
		and (cella['o'] or get_stato(L,k_o)=="Percorso")
		and (cella['e'] or get_stato(L,k_e)=="Percorso")):
		set_stato(L,k,"")
		cammini.remove(k)
		return False
	percorsi=[]
	if not cella['n'] and get_stato(L,k_n)!="Percorso":
		percorsi.append(L[i-1][j])
	if not cella['s'] and get_stato(L,k_s)!="Percorso":
		percorsi.append(L[i+1][j])
	if not cella['e'] and get_stato(L,k_e)!="Percorso":
		percorsi.append(L[i][j+1])
	if not cella['o'] and get_stato(L,k_o)!="Percorso":
		percorsi.append(L[i][j-1])
	for p in percorsi:
		if uscita_pesente(L,p,cammini):
			return True
	set_stato(L,k,"")
	cammini.remove(k)
	return False



# -Parametri: un labirinto (maze) e una cella dello stesso
# -Funzionamento: elimina la presenza di muro su un lato casuale della cella
#  fornita e aggiorna lo stato del labirinto
# -Valore di ritorno: None
def abbatti_muro_random(L,cella):
	i,j=cella['r'],cella['c']
	#vengono identificate le Celle adiacenti
	k=(i,j)
	k_n=(i-1,j)
	k_s=(i+1,j)
	k_e=(i,j+1)
	k_o=(i,j-1)
	possibili_confinanti=[]
	if cella_presente(L,k_n):
		possibili_confinanti.append(k_n)
	if cella_presente(L,k_s):
		possibili_confinanti.append(k_s)
	if cella_presente(L,k_e):
		possibili_confinanti.append(k_e)
	if cella_presente(L,k_o):
		possibili_confinanti.append(k_o)
	if len(possibili_confinanti)>0:
		#estratta a caso una Cella adiacente
		random.shuffle(possibili_confinanti)
		scelta=possibili_confinanti[0]
		del possibili_confinanti[0]
		ic,jc=scelta
		conf=L[ic][jc]
		add_collegata(conf,cella)
		add_collegata(cella,conf)
		#tolto l'eventuale muro fra la Cella cella e la Cella estratta
		if ic<i:
			cella['n']=False
			conf['s']=False
		elif ic>i:
			cella['s']=False
			conf['n']=False
		elif jc<j:
			cella['o']=False
			conf['e']=False
		elif jc>j:
			cella['e']=False
			conf['o']=False



# -Parametri: un labirinto (maze)
# -Funzionamento: per ogni cella del labirinto conta il numero di celle collegate
#  (adiacenti e non separate da muro) e mette mette in una lista tutte le celle
#  con il valore minore
# -Valore di ritorno: la lista delle celle con minor numero di celle adiacenti
#  collegate (non separate da muro)
def cella_poco_connessa(L):
	m=4
	for r in L:
		for c in r:
			if len(c['collegate'])<m:
				m=len(c['collegate'])
			if m==0:
				break
	celle=[]
	for r in L:
		for c in r:
			if len(c['collegate'])==m:
				celle.append(c)
	return celle



# -Parametri: due celle c1 e c2 adiacenti nello stesso labirinto (maze)
# -Funzionamento: aggiunge un muro fra le due celle e aggiorna lo stato del maze
# -Valore di ritorno: None
def metti_muro(c1,c2):
	c1['collegate'].remove(c2)
	c2['collegate'].remove(c1)
	i,j=c1['r'],c1['c']
	ic,jc=c2['r'],c2['c']
	if ic<i:
		c1['n']=True
		c2['s']=True
	elif ic>i:
		c1['s']=True
		c2['n']=True
	elif jc<j:
		c1['o']=True
		c2['e']=True
	elif jc>j:
		c1['e']=True
		c2['o']=True


def importa(file):
	contenuto = []
	#viene letto il contenuto del file in una lista di string
	f = open(file)
	if f==None:
		print "Errore nella lettura del file"
		return None
	for r in f.readlines():
		contenuto.append(r.strip("\n"))
	f.close()
	text_r = len(contenuto)
	if text_r == 0:
		return None
	text_c = 0
	for r in contenuto:
		if len(r)>text_c:
			text_c=len(r)
	#verifica della conformita' del contenuto del file
	for r_i in contenuto:
		if len(r_i) != text_c or contiene_caratteri_non_conformi(r_i):
			print "Errore nel formato del file"
			return None
	r=(text_r-1)/2
	c=(text_c-1)/2
	#inizializzazione della matrice che rappresenta il maze
	maze = []
	for i in range(r):
		maze.append([])
		for j in range(c):
			maze[i].append(None)
	#costruzione della matrice inserendo le Celle in base ai dati del file
	for i in range(r):
		for j in range(c):
			#coordinate della cella nel testo
			t_i=1+2*i
			t_j=1+2*j
			#costruzione della cella
			maze[i][j]=crea_cella(
				r = i,
				c = j,
				n = contenuto[t_i-1][t_j]=='*',
 				s = contenuto[t_i+1][t_j]=='*',
 				o = contenuto[t_i][t_j-1]=='*',
 				e = contenuto[t_i][t_j+1]=='*',
	 			stato = ""
			)
			#aggiornamento delle celle collegate (adiacenti e non separate da muro)
			possibili_collegate=[(i-1,j),(i,j-1)]
			for p_col in possibili_collegate:
				if(cella_presente(maze,p_col) and
					collegate(maze,(i,j),p_col)):
					cella_col=maze[p_col[0]][p_col[1]]
					add_collegata(maze[i][j],cella_col)
					add_collegata(cella_col,maze[i][j])
	return maze



def ben_formato(L):
	#verifica che L rispetti la struttura dati maze
	if len(L)<=0:
		print "L'oggetto non e' un maze"
		return False
	num_c=0
	for r in L:
		if len(r)>num_c:
			num_c=len(r)
	for r in L:
		for elem in r:
			chiavi=['stato','n','s','o','e','r','c','collegate']
			for chiave in chiavi:
				if not chiave in elem:
					print "L'oggetto non e' un maze"
					return False
		#verifica del numero di Celle
		if not len(r) == num_c:
			print "Il numero di celle non e' coerente"
			return False
	#verifica dei campi dato delle Celle
	for i in range(len(L)):
		for j in range(num_c):
			if L[i][j] == None:
				print "manca la cella",(i,j)
				return False
	#verifica corrispondenze fra i muri
	for i in range(len(L)):
		for j in range(num_c):
			c=(i-1,j)
			if(cella_presente(L,c) and
				L[i][j]['n'] != L[c[0]][c[1]]['s']):
				print "Non corrisponde il muro tra",(i,j),"e",c
				return False
			c=(i+1,j)
			if(cella_presente(L,c) and
				L[i][j]['s'] != L[c[0]][c[1]]['n']):
				print "Non corrisponde il muro tra",(i,j),"e",c
				return False
			c=(i,j-1)
			if(cella_presente(L,c) and
				L[i][j]['o'] != L[c[0]][c[1]]['e']):
				print "Non corrisponde il muro tra",(i,j),"e",c
				return False
			c=(i,j+1)
			if(cella_presente(L,c) and
				L[i][j]['e'] != L[c[0]][c[1]]['o']):
				print "Non corrisponde il muro tra",(i,j),"e",c
				return False
	return True



def righe_colonne(L):
	if len(L) == 0:
		return (0,0)
	return (len(L),len(L[0]))



def uscite(L):
	u = []
	r,c=righe_colonne(L)
	for j in range(c):
		if L[0][j]['n'] == False:
			if not (0,j) in u:
				u.append((0,j))
		if L[r-1][j]['s'] == False:
			if not (r-1,j) in u:
				u.append((r-1,j))
	for i in range(r):
		if L[i][0]['o'] == False:
			if not (i,0) in u:
				u.append((i,0))
		if L[i][c-1]['e'] == False:
			if not (i,c-1) in u:
				u.append((i,c-1))
	return u



def aggiungi_uscita(L):
	r,c=righe_colonne(L)
	possibili_uscite=[]
	#creazione lista possibili uscite
	for j in range(c):
		possibili_uscite.append((0,j))
		possibili_uscite.append((r-1,j))
	for i in range(r):
		possibili_uscite.append((i,0))
		possibili_uscite.append((i,c-1))
	#estrazione casuale
	random.shuffle(possibili_uscite)
	u=None
	while len(possibili_uscite)>0 and u==None:
		u1=possibili_uscite[0]
		del possibili_uscite[0]
		if not u1 in uscite(L):
			u=u1
	if u != None:
		ui,uj=u
		if ui==0:
			L[ui][uj]['n']=False
		elif ui==r-1:
			L[ui][uj]['s']=False
		elif uj==0:
			L[ui][uj]['o']=False
		elif uj==c-1:
			L[ui][uj]['e']=False



def muri(L,c):
	if not cella_presente(L,c):
		print "Cella non presente nel labirinto"
		return {}
	i,j=c
	m=dict()
	m['N']=L[i][j]['n']
	m['S']=L[i][j]['s']
	m['E']=L[i][j]['e']
	m['O']=L[i][j]['o']
	return m



def collegate(L,c1,c2):
	if not cella_presente(L,c1) or not cella_presente(L,c2):
		print "c1 o c2 non presenti"
		return False
	if not adiacenti(c1,c2):
		print "celle non adiacenti"
		return False
	if c1[0] > c2[0]: # c1[1]==c2[1] perche' adiacenti
		return not L[c1[0]][c1[1]]['n']
	elif c1[0] < c2[0]: # c1[1]==c2[1] perche' adiacenti
		return not L[c1[0]][c1[1]]['s']
	elif c1[1] > c2[1]: # c1[0]==c2[0]
		return not L[c1[0]][c1[1]]['o']
	elif c1[1] < c2[1]: # c1[0]==c2[0]
		return not L[c1[0]][c1[1]]['e']
	return False



def get_stato(L,c):
	if not cella_presente(L,c):
		print "Cella non presente"
		return None
	i,j=c
	return L[i][j]['stato']



def set_stato(L,c,s):
	if cella_presente(L,c):
		i,j=c
		L[i][j]['stato'] = s
	else:
		print "Cella non presente"



def stampa(L):
	r,c = righe_colonne(L)
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
			if L[i][j]['o']:
				if L[i][j]['stato'] == 'Percorso':
					line+="| P "
				else:
					line+="|   "
			else:
				if L[i][j]['stato'] == 'Percorso':
					line+="  P "
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



def perfetto(L):
	if L == None:
		print "Labirinto non ben definito"
		return False
	#se sono presenti cicli il labirinto non e' perfetto
	if contiene_ciclo(L):
		return False
	#Non ci sono cicli ed e' possibile invocare la funzione connesso() per
	#verificare che il labirinto sia connesso
	return connesso(L)



def risolvi_alla_cieca(L,partenza):
	r,c=righe_colonne(L)
	#azzera lo stato delle Celle del labirinto
	for h in range(r):
		for k in range(c):
			coord=(h,k)
			set_stato(L,coord,"")
	i,j=partenza
	cella=L[i][j]
	percorso=[]
	uscita_pesente(L,cella,percorso)
	#dato che il labirinto e' ben formato e perfetto per ipotesi il cammino
	#dalla cella ad una uscita del labirinto
	#esiste sempre e viene salvato dalla funzione uscita_presente nella lista
	#percorso, che viene quindi restituita
	return percorso



def trova_percorso(L,c1,c2):
	i,j=c1
	h,k=c2
	inizio=L[i][j]
	fine=L[h][k]
	percorso=[]
	#dato che il labirinto e' ben formato e perfetto per ipotesi, esiste
	#sempre un cammino da c1 a c2, che viene trovato dalla funzione esiste_cammino
	esiste_cammino(inizio,fine,percorso)
	p=[]
	for c in percorso:
		p.append((c['r'],c['c']))
	return p



def genera_labirinto(r,c):
	#viene istanziato un maze iniziale dove ogni Cella ha tutti i muri su ogni lato
	L=[]
	for i in range(r):
		L.append([])
		for j in range(c):
			L[i].append(crea_cella(i,j))
	#per ogni Cella viene abbattuto un muro scelto in modo random
	for l in L:
		for cella in l:
			abbatti_muro_random(L,cella)
	#la funzione cicla fino a che non si ottiene un maze perfetto
	while not ben_formato(L) or not perfetto(L):
		ciclo=[]
		#si tolgono eventuali cicli presenti nel maze cercandoli e mettendo
		#un muro fra le ultime due Celle dell'eventuale ciclo trovato
		while contiene_ciclo(L):
			trova_ciclo(L,ciclo)
			c1=ciclo[len(ciclo)-1]
			del ciclo[len(ciclo)-1]
			c2=ciclo[len(ciclo)-1]
			del ciclo[len(ciclo)-1]
			ciclo=[]
			metti_muro(c1,c2)
		#ciclo che continua fino a che il grafo del labirinto non risulta
		#essere connesso (non vi sono cicli a questo punto, quindi
		#puo' essere usata la funzione connesso)
		while not connesso(L):
			#viene abbattuto un muro a caso nelle Celle che presentano un
			#maggior numero di muri
			for k in cella_poco_connessa(L):
				abbatti_muro_random(L,k)
			#vengono tolti eventuali cicli introdotti
			while contiene_ciclo(L):
				trova_ciclo(L,ciclo)
				c1=ciclo[len(ciclo)-1]
				del ciclo[len(ciclo)-1]
				c2=ciclo[len(ciclo)-1]
				del ciclo[len(ciclo)-1]
				ciclo=[]
				metti_muro(c1,c2)
	return L



# --- Test ---

# L = importa("maze.txt")
# print ben_formato(L)
# print righe_colonne(L)
# print uscite(L)
# print muri(L,(1,3))
# print muri(L,(2,3))
# print collegate(L,(1,3),(2,3))
# aggiungi_uscita(L)
# stampa(L)
# print perfetto(L)
# print connesso(L)
# print contiene_ciclo(L)
# print risolvi_alla_cieca(L,(0,0))
# stampa(L)
# print trova_percorso(L,(1,1),(4,4))
# add_collegata(L[0][2],L[0][1])
# kk=[]
# print contiene_ciclo(L,kk)
# print [(p['r'],p['c']) for p in kk]
L = genera_labirinto(15,15)
stampa(L)
print "From (1,1) to (14,14):"
w = trova_percorso(L,(1,1),(14,14))
print w
for x in w:
	set_stato(L,x,'Percorso')
stampa(L)
