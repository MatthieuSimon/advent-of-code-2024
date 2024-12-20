from heapq import heappush, heappop

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    pq = []
    heappush(pq, (0, start, (0, -1), [start]))
    visited = {}

    while pq:
        cost, current, prev_dir, path = heappop(pq)
        
        if current == end:
            return cost
        
        if current in visited and visited[current] <= cost:
            continue
        
        visited[current] = cost

        for (dr, dc) in directions:
            nr, nc = current[0] + dr, current[1] + dc
            next_pos = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                turn_cost = 1000 if prev_dir is not None and prev_dir != (dr, dc) else 0
                move_cost = 1
                total_cost = cost + turn_cost + move_cost
                
                heappush(pq, (total_cost, next_pos, (dr, dc), path + [next_pos]))

def main():
    grid = []
    start, end = (), ()
    with open("../input.txt") as file:
        grid = [line.strip() for line in file]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    result = dijkstra(grid, start, end)
    print(result)
    
if __name__ == "__main__":
    main()