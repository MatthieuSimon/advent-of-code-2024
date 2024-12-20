from itertools import count

def display(robots):
    grid = [[" " for _ in range(101)] for _ in range(103)]
    for x, y in robots:
        grid[y][x] = "x"
    print("\n".join(map(" ".join, grid)))

def main():    
    with open("../input.txt") as file:
        data = []
        for line in file.readlines():
            line = line.strip()
            parts = line.split(' ')
            p = parts[0].split('=')[1]
            v = parts[1].split('=')[1]
            data.append([list(map(int, p.split(','))), list(map(int, v.split(',')))])

    min_sf = float("inf")
    width = 101
    height = 103
    for second in count():
        q1, q2, q3, q4 = 0, 0, 0, 0
        robots_after = []
        for robot in data:
            pos, velocity = robot
            robots_after.append(((pos[0] + velocity[0] * second) % width, (pos[1] + velocity[1] * second) % height))
        for px, py in robots_after:
            if px == width // 2 or py == height // 2:
                continue
            if px < width // 2 and py < height // 2:
                q1 += 1
            elif px > width // 2 and py < height // 2:
                q2 += 1
            elif px < width // 2 and py > height // 2:
                q3 += 1
            else:
                q4 += 1
        result = q1 * q2 * q3 * q4
        if result < min_sf:
            min_sf = result
            display(robots_after)
            a = input()
            if a and a in "y":
                print(second)
                exit()
    
if __name__ == "__main__":
    main()