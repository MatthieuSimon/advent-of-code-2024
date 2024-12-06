import copy

def direction_by_value(direction):
    direction_map = {
        (1, 0): 'R',
        (0, 1): 'B',
        (-1, 0): 'L',
        (0, -1): 'T'
    }
    # Return the next direction
    return direction_map[direction]

def rotate(direction):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    next_direction = (directions.index(direction) + 1) % len(directions)
    return directions[next_direction]

def move_guard(guard_position, direction, map):
    x, y = guard_position
    dir_x, dir_y = direction
    if y + dir_y < 0 or y + dir_y >= len(map) or x + dir_x < 0 or x + dir_x >= len(map[y]):
        raise ValueError("Out of bounds")
    if map[y + dir_y][x + dir_x] == "#" or map[y + dir_y][x + dir_x] == "O":
        return move_guard(guard_position, rotate(direction), map)
    else:
        if map[y + dir_y][x + dir_x] in ["T", "B", "L", "R"] and direction_by_value(direction) == map[y + dir_y][x + dir_x]:
            raise Exception("Stuck")
        return (x + dir_x, y + dir_y), direction

def find_guard_and_set_default_direction(map):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == '^':
                return (x, y), (0, -1)

def compute_map(map_to_compute):
    guard_position, direction = find_guard_and_set_default_direction(map_to_compute)
    while True:
        try:
            guard_position, direction = move_guard(guard_position, direction, map_to_compute)
            x, y = guard_position
            map_to_compute[y][x] = direction_by_value(direction)
        except ValueError:
            print("He's out")
            break
    return map_to_compute

def main():
    with open("../input.txt", 'r') as file:
        start_map = [list(line.strip()) for line in file]
        copy_map = copy.deepcopy(start_map)
        end_map = compute_map(copy_map)
        all_maps = []

        for y in range(len(end_map)):
            for x in range(len(end_map[y])):
                if end_map[y][x] in ["X", "T", "B", "L", "R"]:
                    new_map = copy.deepcopy(start_map)
                    new_map[y][x] = "O"
                    all_maps.append(new_map)
        nb_loops = 0
        for m in all_maps:
            try:
                _, _ = compute_map(m)
            except Exception as e:
                if str(e) == "Stuck":
                    nb_loops += 1
                    continue
            except ValueError as e:
                continue
        print(nb_loops)

if __name__ == "__main__":
    main()