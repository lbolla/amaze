import heapq
import math
import random
import time


def print_grid(grid):
    print('\033c')
    m = {
        0: ' ',
        1: "\033[91m▄\033[00m",
        2: '.',
        3: "\033[92m▄\033[00m",
        4: "\033[93m▄\033[00m",
        9: "\033[95m▄\033[00m",
    }
    for row in grid:
        for item in row:
            print(m[item], end=' ')
        print()


def animate_grid(grid):
    # print_grid(grid)
    # time.sleep(0.01)
    pass


def generate_dfs(n, m):
    grid = []
    for i in range(2 * N + 1):
        grid.append([2] * (2 * M + 1))

    carve(grid, 1, 1)

    start = (1, 0)
    end = (2 * N - 1, 2 * M)
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0
    return grid, start, end


def carve(grid, x, y):

    def get_adjacent(grid, x, y):
        N = len(grid)
        M = len(grid[0])
        directions = [
            (2, 0),
            (-2, 0),
            (0, 2),
            (0, -2),
        ]
        random.shuffle(directions)
        for direction in directions:
            cell_x = x + direction[0]
            cell_y = y + direction[1]
            if (
                    0 <= cell_x < N and
                    0 <= cell_y < M and
                    grid[cell_x][cell_y] == 2
            ):
                yield (cell_x, cell_y)

    grid[x][y] = 0
    animate_grid(grid)
    for cell_x, cell_y in get_adjacent(grid, x, y):
        for i in range(min(x, cell_x), max(x, cell_x) + 1):
            grid[i][y] = 0
        for j in range(min(y, cell_y), max(y, cell_y) + 1):
            grid[x][j] = 0
        carve(grid, cell_x, cell_y)


def generate_kruskal(n, m):
    grid = []
    for i in range(2 * N + 1):
        grid.append([2] * (2 * M + 1))

    kruskal(grid)

    start = (1, 0)
    end = (2 * N - 1, 2 * M)
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0
    return grid, start, end


def kruskal(grid):
    # for all edges of graph
    # if u and v belong to diff comp, union them
    N = len(grid)
    M = len(grid[0])
    edges = []
    nodes = set()
    for i in range(1, N, 2):
        for j in range(1, M, 2):
            u = (i, j)
            grid[i][j] = 0
            nodes.add(u)
            if i + 2 < N:
                v = (i + 2, j)
                grid[i + 2][j] = 0
                nodes.add(v)
                edges.append((u, v))
            if j + 2 < M:
                v = (i, j + 2)
                grid[i][j + 2] = 0
                nodes.add(v)
                edges.append((u, v))
    random.shuffle(edges)

    uf = UnionFind(nodes)
    for u, v in edges:
        if not uf.same_component(u, v):
            uf.union(u, v)
            w = ((u[0] + v[0]) // 2, (u[1] + v[1]) // 2)
            grid[w[0]][w[1]] = 0

            animate_grid(grid)


class UnionFind:
    def __init__(self, nodes):
        self.parents = {u: u for u in nodes}
        self.sizes = {u: 1 for u in nodes}

    def find(self, v):
        if self.parents[v] == v:
            return v
        return self.find(self.parents[v])

    def same_component(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.sizes[pu] > self.sizes[pv]:
            self.parents[pv] = pu
            self.sizes[pu] += self.sizes[pv]
        else:
            self.parents[pu] = pv
            self.sizes[pv] += self.sizes[pu]


def generate_prim(n, m):
    grid = []
    for i in range(2 * N + 1):
        grid.append([2] * (2 * M + 1))

    prim(grid)

    start = (1, 0)
    end = (2 * N - 1, 2 * M)
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0
    return grid, start, end


def prim(grid):
    N = len(grid)
    M = len(grid[0])

    def get_walls(u):
        directions = [
            (2, 0),
            (-2, 0),
            (0, 2),
            (0, -2),
        ]
        x, y = u
        for direction in directions:
            xx = x + direction[0]
            yy = y + direction[1]
            if 0 <= xx < N and 0 <= yy < M:
                yield (u, (xx, yy))

    seen = set()
    walls = list()

    u = (1, 1)
    grid[u[0]][u[1]] = 0
    seen.add(u)
    walls.extend(get_walls(u))
    while walls:
        i = random.randrange(len(walls))
        u, v = walls.pop(i)
        grid[u[0]][u[1]] = 0
        grid[v[0]][v[1]] = 0
        animate_grid(grid)
        if v not in seen or u not in seen:
            unseen = v if v not in seen else u
            w = ((u[0] + v[0]) // 2, (u[1] + v[1]) // 2)
            grid[w[0]][w[1]] = 0
            seen.add(unseen)
            walls.extend(get_walls(unseen))


def solve_dfs(grid, start, end):

    def get_adjacent(grid, p):
        N = len(grid)
        M = len(grid[0])
        x, y = p
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        # random.shuffle(directions)
        for direction in directions:
            cell_x = x + direction[0]
            cell_y = y + direction[1]
            if (
                    0 <= cell_x < N and
                    0 <= cell_y < M and
                    grid[cell_x][cell_y] == 0
            ):
                yield (cell_x, cell_y)

    parents = {}
    stack = []
    stack.insert(0, start)
    while stack:
        animate_grid(grid)

        curr = stack.pop(0)
        grid[curr[0]][curr[1]] = 1

        if curr == end:
            color_path(grid, end, parents)
            return

        for cell in get_adjacent(grid, curr):
            stack.insert(0, cell)
            parents[cell] = curr


def solve_bfs(grid, start, end):

    def get_adjacent(grid, p):
        N = len(grid)
        M = len(grid[0])
        x, y = p
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        # random.shuffle(directions)
        for direction in directions:
            cell_x = x + direction[0]
            cell_y = y + direction[1]
            if (
                    0 <= cell_x < N and
                    0 <= cell_y < M and
                    grid[cell_x][cell_y] == 0
            ):
                yield (cell_x, cell_y)

    queue = []
    queue.append(start)
    parents = {}
    while queue:
        animate_grid(grid)

        curr = queue.pop(0)
        grid[curr[0]][curr[1]] = 3

        if curr == end:
            color_path(grid, end, parents)
            return

        for cell in get_adjacent(grid, curr):
            queue.append(cell)
            parents[cell] = curr


def solve_opt(grid, start, end):

    def get_adjacent(grid, p):
        N = len(grid)
        M = len(grid[0])
        x, y = p
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        for direction in directions:
            cell_x = x + direction[0]
            cell_y = y + direction[1]
            if (
                    0 <= cell_x < N and
                    0 <= cell_y < M and
                    grid[cell_x][cell_y] == 0
            ):
                yield (cell_x, cell_y)

    def dist(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    parents = {}
    queue = []
    heapq.heappush(queue, (dist(start, end), start))
    while queue:
        animate_grid(grid)

        _, curr = heapq.heappop(queue)
        grid[curr[0]][curr[1]] = 4

        if curr == end:
            color_path(grid, end, parents)
            return

        for cell in get_adjacent(grid, curr):
            heapq.heappush(queue, (dist(cell, end), cell))
            parents[cell] = curr


def color_path(grid, end, parents):
    curr = end
    while curr:
        grid[curr[0]][curr[1]] = 9
        curr = parents.get(curr)


N, M = 25, 52
# N, M = 3, 4
# grid, start, end = generate_dfs(N, M)
# grid, start, end = generate_kruskal(N, M)
grid, start, end = generate_prim(N, M)

# solve_dfs(grid, start, end)
# solve_bfs(grid, start, end)
solve_opt(grid, start, end)
print_grid(grid)
