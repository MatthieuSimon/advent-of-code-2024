def char_to_direction(value):
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    return directions.get(value)

def move_next(x, y, dx, dy, grid):
    next_x, next_y = x + dx, y + dy
    while grid[next_x][next_y] == "O":
        next_x += dx
        next_y += dy
    if grid[next_x][next_y] == ".":
        grid[next_x][next_y] = grid[next_x - dx][next_y - dy]
        grid[x][y] = "."
        x += dx
        y += dy
        grid[x][y] = "@"
    return x, y
    
def main():
    grid = []
    instructions = []
    with open("../input.txt") as file:
        while line := file.readline().strip():
            grid.append(list(line))
        while line := file.readline().strip():
            instructions.append(line)
        instructions = "".join(instructions)
    robot_x, robot_y = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]
    for move in instructions:
        robot_x, robot_y = move_next(robot_x, robot_y, *char_to_direction(move), grid)
    answer = sum(100 * i + j for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "O")
    print(answer)
    
if __name__ == "__main__":
    main()