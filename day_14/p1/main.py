def main():    
    with open("../input.txt") as file:
        data = []
        for line in file.readlines():
            line = line.strip()
            parts = line.split(' ')
            p = parts[0].split('=')[1]
            v = parts[1].split('=')[1]
            data.append([list(map(int, p.split(','))), list(map(int, v.split(',')))])
            print(data)
    q1= 0
    q2 = 0
    q3 = 0
    q4 = 0
    width = 101
    height = 103
    seconds = 100
    for robot in data:
        pos, velocity = robot
        pos[0] = (pos[0] + velocity[0] * seconds) % width
        pos[1] = (pos[1] + velocity[1] * seconds) % height
        if pos[0] == width // 2 or pos[1] == height // 2:
            continue
        if pos[0] < width // 2 and pos[1] < height // 2:
            q1 += 1
        elif pos[0] > width // 2 and pos[1] < height // 2:
            q2 += 1
        elif pos[0] < width // 2 and pos[1] > height // 2:
            q3 += 1
        else:
            q4 += 1
    print(q1 * q2 * q3 * q4)

    
if __name__ == "__main__":
    main()