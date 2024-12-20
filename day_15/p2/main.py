def char_to_direction(value):
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    return directions.get(value)

def can_be_pushed(x, y, dx, dy, grid):
    if grid[x + dx][y + dy] == "#":
        return False
    elif grid[x + dx][y + dy] == ".":
        return True
    elif dx: # UP or DOWN
        if grid[x + dx][y + dy] == "[":
            return (can_be_pushed(x + dx, y, dx, dy, grid) and
                    can_be_pushed(x + dx, y + 1, dx, dy, grid))
        elif grid[x + dx][y + dy] == "]":
            return (can_be_pushed(x + dx, y - 1, dx, dy, grid) and
                    can_be_pushed(x + dx, y, dx, dy, grid))
    else: # LEFT or RIGHT
        return can_be_pushed(x, y + dy, dx, dy, grid)

def push_box(x, y, dx, dy, grid):
    if grid[x + dx][y + dy] == "[":
        push_box(x + dx, y + dy, dx, dy, grid)
        if dx: # UP or DOWN
            push_box(x + dx, y + 1, dx, dy, grid)
    elif grid[x + dx][y + dy] == "]":
        push_box(x + dx, y + dy, dx, dy, grid)
        if dx: # UP or DOWN
            push_box(x + dx, y - 1, dx, dy, grid)
    grid[x + dx][y + dy] = grid[x][y]
    grid[x][y] = "."

def move_next(x, y, dx, dy, grid):
        if can_be_pushed(x, y, dx, dy, grid):
            push_box(x, y, dx, dy, grid)
            x += dx
            y += dy
        return x, y

def draw_grid(grid):
    for line in grid:
        print(line)

def main():
    grid = []
    instructions = []
    with open("../input.txt") as file:
        while line := file.readline().strip():
            bigger_grid = []
            for c in line:
                if c == "#":
                    bigger_grid.extend(["#", "#"])
                elif c == ".":
                    bigger_grid.extend([".", "."])
                elif c == "O":
                    bigger_grid.extend(["[", "]"])
                elif c == "@":
                    bigger_grid.extend(["@", "."])
            # print(bigger_grid)
            grid.append(bigger_grid)
        while line := file.readline().strip():
            instructions.append(line)
        instructions = "".join(instructions)
    robot_x, robot_y = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]
    for move in instructions:
        robot_x, robot_y = move_next(robot_x, robot_y, *char_to_direction(move), grid)
        # draw_grid(grid)
        # print("\n")
    answer = sum(100 * i + j for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "[")
    print(answer)
    
if __name__ == "__main__":
    main()