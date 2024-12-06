def rotate(direction):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    next_direction = (directions.index(direction) + 1) % len(directions)
    return directions[next_direction]

def move_guard(guard_position, direction, map):
    x, y = guard_position
    dir_x, dir_y = direction
    if y + dir_y < 0 or y + dir_y >= len(map) or x + dir_x < 0 or x + dir_x >= len(map[y]):
        raise ValueError("Out of bounds")
    if map[y + dir_y][x + dir_x] == "#":
        return move_guard(guard_position, rotate(direction), map)
    else:
        return (x + dir_x, y + dir_y), direction

def find_guard_and_set_default_direction(map):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == '^':
                return (x, y), (0, -1)

def main():
    with open("../input.txt", 'r') as file:
        map = [list(line.strip()) for line in file]
        guard_position, direction = find_guard_and_set_default_direction(map)

        while True:
            try:
                guard_position, direction = move_guard(guard_position, direction, map)
                x, y = guard_position
                map[y][x] = "X"
            except ValueError:
                print("He's out")
                break        
        print(sum(row.count('X') for row in map))

if __name__ == "__main__":
    main()