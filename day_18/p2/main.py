from heapq import heappush, heappop

def dijkstra(grid, start, end):
    score = 1
    current = start
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heappush(pq, (score, current, [current]))
    visited = set()
    while pq:
        score, current, current_route = heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        for (dr, dc) in directions:
            nr, nc = current[0] + dr, current[1] + dc
            next_pos = (nr, nc)
            if next_pos == end:
                return score
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '.':
                heappush(pq, (score + 1, next_pos, current_route + [next_pos]))
    return None

def main():
    kilobyte = 1024
    size = 71
    grid = [['.' for _ in range(size)] for _ in range(size)]
    start, end = (0, 0), (size - 1, size - 1)
    i = 0
    with open("../input.txt") as file:
        for line in file.readlines():
            x, y = map(int, line.strip().split(','))
            grid[y][x] = '#'
            if i > kilobyte:
                result = dijkstra(grid, start, end)
                if result is None:
                    print(x,y)
                    break
            i += 1

if __name__ == "__main__":
    main()