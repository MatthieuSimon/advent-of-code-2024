def main():
    file=open("../input.txt",'r') 
    data = file.read().splitlines()
    content = []
    for line in data:
        content.append([])
        for char in line:
            content[-1].append(char)
    antenna_to_pos = {}

    for i, row in enumerate(content):
        for j, value in enumerate(row):
            if value != ".":
                antenna_to_pos.setdefault(value, []).append((i, j))

    for antenna in antenna_to_pos.keys():
        for (x, y) in antenna_to_pos[antenna]:
            for (i, j) in antenna_to_pos[antenna]:
                gap = (x-i, y-j)
                if gap[0] == 0 and gap[1] == 0:
                    continue

                n = len(content) * len(content[0])
                for i in range(-n, n):
                    new_gap = (gap[0]*i, gap[1]*i)
                    antinode = (x+new_gap[0], y+new_gap[1])
                    if 0 <= antinode[0] < len(content) and 0 <= antinode[1] < len(content[0]):
                        content[antinode[0]][antinode[1]] = "#"
    res = ("\n".join(["".join(line) for line in content]))
    print(res.count("#"))

if __name__ == "__main__":
    main()