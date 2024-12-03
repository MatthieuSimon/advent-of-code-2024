def main():
    file=open("../input.txt",'r') 
    row = file.readlines()
    safe = 0
    for line in row:
        list_line = [int(i) for i in line.split()]
        print(list_line)
        is_safe = all(1 <= list_line[i] - list_line[i + 1] <= 3 for i in range(len(list_line) - 1)) or all(-1 >= list_line[i] - list_line[i + 1] >= -3 for i in range(len(list_line) - 1))
        print(is_safe)
        if is_safe:
            safe += 1
    print(safe)

if __name__ == "__main__":
    main()