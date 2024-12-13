def check_path(grid, zero, row_length, column_length, found):
    found.append(zero)
    row_value, col_value, value = zero
    # print(zero)
    if value == 9:
        return 1
    
    result = 0

    for row_direction, col_direction in [(-1, 0), (1,0), (0, 1), (0, -1)]:
        next_row, next_col = row_value + row_direction, col_value + col_direction
        next_check = (next_row, next_col, value + 1)
        if 0 <= next_row < row_length and 0 <= next_col < column_length and grid[next_row][next_col] == value + 1 and next_check not in found: 
            result += check_path(grid, next_check, row_length, column_length, found)

    return result

def main():
    file=open("../input.txt",'r') 
    grid = [[int(c) for c in l] for l in file.read().split()]
    row_length = len(grid)
    column_length = len(grid[0])

    zeros = [(row, col, 0) for row in range(row_length) for col in range(column_length) if grid[row][col] == 0]

    print(zeros)

    result = 0
    for z in zeros:
        result += check_path(grid, z, row_length, column_length, [])

    print(result)

if __name__ == "__main__":
    main()