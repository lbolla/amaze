# aMaze

These are some experiments with maze generators and solvers.

See https://en.wikipedia.org/wiki/Maze_generation_algorithm

Generators:

- DFS
- Kruskal
- Prim

Solvers:

- DFS
- BFS
- OPT, heuristic based BFS

DFS generator tends to produce more convoluted mazes than Kruskal or
Prim.

![dfs-opt](dfs-opt.png "DFS maze with OPT solver")
![kruskal-dfs](kruskal-dfs.png "Kruskal maze with DFS solver")
![kruskal-bfs](kruskal-bfs.png "Kruskal maze with BFS solver")
![kruskal-opt](kruskal-opt.png "Kruskal maze with OPT solver")
![prim-opt](prim-opt.png "Prim maze with OPT solver")
