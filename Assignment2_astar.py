import heapq
import time

# Grid yang sama
grid = [
    ['S', '.', '.', '.', 'T'],
    ['T', 'T', '.', 'T', '.'],
    ['.', '.', '.', '.', '.'],
    ['T', 'T', '.', 'T', 'T'],
    ['.', '.', '.', '.', 'H']
]

rows = len(grid)
cols = len(grid[0])

# Fungsi heuristik: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Cari posisi S dan H
def find_pos(symbol):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == symbol:
                return (r, c)
    return None

# A* Algorithm
def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    node_count = 0

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        node_count += 1

        if current == goal:
            return path, node_count

        if current in visited:
            continue
        visited.add(current)

        r, c = current
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != 'T' and (nr, nc) not in visited:
                    new_g = g + 1  # cost uniform
                    new_f = new_g + heuristic((nr, nc), goal)
                    heapq.heappush(open_set, (new_f, new_g, (nr, nc), path + [(nr, nc)]))

    return None, node_count

# Jalankan A*
start = find_pos('S')
goal = find_pos('H')

start_time = time.time()
path, nodes = astar(start, goal)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000

# Visualisasi
def print_grid_with_path(path):
    for r in range(rows):
        for c in range(cols):
            if (r, c) in path and grid[r][c] not in ['S', 'H']:
                print('*', end=' ')
            else:
                print(grid[r][c], end=' ')
        print()

print("A* Path:", path)
print("Nodes Expanded:", nodes)
print("Time (ms):", elapsed_time)
print("\nPath Visualization:")
print_grid_with_path(path)
