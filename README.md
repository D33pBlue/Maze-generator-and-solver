# Maze-generator-and-solver
Maze generator (that can generate a maze of custom size) and solver (though graph analysis)

Example:

14*14 generated maze:
```
+---+---+---+---+---+---+---+---+---+---+---+---+   +---+
|                       |               |               |
+   +---+---+---+---+   +   +---+---+   +---+---+---+   +
|   |                   |   |       |       |       |   |
+   +   +---+---+---+---+---+   +   +   +   +   +   +   +
|   |   |       |           |   |   |   |   |   |       |
+   +   +---+   +   +   +   +   +---+   +   +   +---+---+
|   |   |           |   |   |   |       |   |       |   |
+   +   +   +---+---+---+   +   +   +---+   +---+   +   +
|   |   |               |   |   |       |           |   |
+   +   +---+---+---+   +   +   +---+   +---+---+   +   +
|   |               |   |   |       |           |   |   |
+   +---+---+   +   +   +   +---+   +---+---+   +   +   +
|   |       |   |       |       |           |   |   |   |
+   +   +   +   +---+---+---+   +---+---+   +   +   +   +
|   |   |   |   |           |   |       |       |   |   |
+---+---+   +   +   +---+   +   +   +   +---+---+   +   +
|       |   |       |       |       |               |   |
+   +   +   +---+---+   +   +---+---+---+   +---+---+   +
|   |               |   |       |       |   |       |   |
+   +---+---+---+   +   +---+   +   +   +   +   +   +   +
|   |       |       |       |       |   |   |   |   |   |
+   +---+   +   +---+---+   +---+---+   +   +   +   +   +
|   |       |   |       |       |   |   |   |   |       |
+   +   +---+   +   +   +---+   +   +   +   +   +---+---+
|   |       |       |       |   |   |   |   |           |
+   +   +   +---+---+---+   +   +   +   +   +---+---+   +
|       |               |       |       |               |
+   +---+---+---+---+---+---+---+---+---+---+---+---+---+
```

Solution:
[(13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (8, 1), (9, 1), (9, 2), (9, 3), (9, 4), (10, 4), (10, 3), (11, 3), (12, 3), (12, 4), (11, 4), (11, 5), (12, 5), (12, 6), (13, 6), (13, 7), (12, 7), (11, 7), (11, 6), (10, 6), (10, 5), (9, 5), (8, 5), (8, 6), (7, 6), (7, 5), (7, 4), (8, 4), (8, 3), (7, 3), (6, 3), (5, 3), (5, 4), (6, 4), (6, 5), (5, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 7), (7, 7), (8, 7), (8, 8), (7, 8), (7, 9), (8, 9), (8, 10), (8, 11), (8, 12), (7, 12), (6, 12), (5, 12), (4, 12), (3, 12), (3, 11), (2, 11), (1, 11), (1, 12), (2, 12), (2, 13), (1, 13), (0, 13), (0, 12)]

```
+---+---+---+---+---+---+---+---+---+---+---+---+   +---+
|                       |               |         X   X |
+   +---+---+---+---+   +   +---+---+   +---+---+---+   +
|   |                   |   |       |       | X   X | X |
+   +   +---+---+---+---+---+   +   +   +   +   +   +   +
|   |   |       | X   X   X |   |   |   |   | X | X   X |
+   +   +---+   +   +   +   +   +---+   +   +   +---+---+
|   |   | X   X   X |   | X |   |       |   | X   X |   |
+   +   +   +---+---+---+   +   +   +---+   +---+   +   +
|   |   | X   X   X   X | X |   |       |         X |   |
+   +   +---+---+---+   +   +   +---+   +---+---+   +   +
|   |         X   X | X | X |       |           | X |   |
+   +---+---+   +   +   +   +---+   +---+---+   +   +   +
|   |       | X | X   X | X   X |           |   | X |   |
+   +   +   +   +---+---+---+   +---+---+   +   +   +   +
|   |   |   | X | X   X   X | X | X   X |       | X |   |
+---+---+   +   +   +---+   +   +   +   +---+---+   +   +
| X   X |   | X   X | X   X | X   X | X   X   X   X |   |
+   +   +   +---+---+   +   +---+---+---+   +---+---+   +
| X | X   X   X   X | X |       |       |   |       |   |
+   +---+---+---+   +   +---+   +   +   +   +   +   +   +
| X |       | X   X | X   X |       |   |   |   |   |   |
+   +---+   +   +---+---+   +---+---+   +   +   +   +   +
| X |       | X | X   X | X   X |   |   |   |   |       |
+   +   +---+   +   +   +---+   +   +   +   +   +---+---+
| X |       | X   X | X   X | X |   |   |   |           |
+   +   +   +---+---+---+   +   +   +   +   +---+---+   +
| X     |               | X   X |       |               |
+   +---+---+---+---+---+---+---+---+---+---+---+---+---+
```
