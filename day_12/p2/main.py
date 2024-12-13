def count_sides(pos, c, map):
    x, y = pos
    sides = 0
    
    normal_pairs = [
        ((0, -1), (1, 0)),
        ((0, -1), (-1, 0)),
        ((0, 1), (1, 0)),
        ((0, 1), (-1, 0))
    ]
    for d1, d2 in normal_pairs:
        if map[(x + d1[0], y + d1[1])] != c and map[(x + d2[0], y + d2[1])] != c:
            sides += 1

    negative_triplets = [
        ((0, -1), (-1, 0), (-1, -1)),
        ((0, -1), (1, 0), (1, -1)),
        ((0, 1), (-1, 0), (-1, 1)),
        ((0, 1), (1, 0), (1, 1))
    ]
    for d1, d2, d3 in negative_triplets:
        if (map[(x + d1[0], y + d1[1])] == c and 
            map[(x + d2[0], y + d2[1])] == c and 
            map[(x + d3[0], y + d3[1])] != c):
            sides += 1

    return sides

def main():
    file=open("../input.txt",'r')
    result = 0
    map = {}
    for r, row in enumerate(file.readlines()):
        for c, char in enumerate(row.strip()):
            map[(r, c)] = char
    max_x = max(map.keys(), key=lambda c: c[0])[0]
    max_y = max(map.keys(), key=lambda c: c[1])[1]
    for x in range(-1, max_x + 2):
        map[(x, -1)] = '?'
        map[(x, max_y + 1)] = '?'
    for y in range(-1, max_y + 2):
        map[(-1, y)] = '?'
        map[(max_x + 1, y)] = '?'
    processed = set()
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if (x, y) in processed:
                continue
            area = 0
            sides = 0
            to_visit = [(x, y)]
            c = map[(x, y)]
            while to_visit:
                pos = to_visit.pop()
                if pos in processed:
                    continue
                processed.add(pos)
                area += 1
                around = []
                for neib in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x = pos[0] + neib[0]
                    new_y =  pos[1] + neib[1]
                    if  new_x >= 0 and new_x <= max_x and new_y >= 0 and new_y <= max_y and c == map[(new_x, new_y)]:
                        around.append((new_x, new_y))
                sides += count_sides(pos, c, map)
                to_visit.extend(around)
            result += area * sides
    print(result)

if __name__ == "__main__":
    main()