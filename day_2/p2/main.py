def check_is_safe(list_line):
    return all(1 <= list_line[i] - list_line[i + 1] <= 3 for i in range(len(list_line) - 1)) or all(-1 >= list_line[i] - list_line[i + 1] >= -3 for i in range(len(list_line) - 1))

def main():
    file=open("../input.txt",'r') 
    row = file.readlines()
    safe = 0
    for line in row:
        list_line = [int(i) for i in line.split()]
        is_safe = check_is_safe(list_line)
        if is_safe:
            safe += 1
        else:
            for i in range(len(list_line)):
                updated_line = list_line.copy()
                updated_line.pop(i)
                if check_is_safe(updated_line) :
                    safe += 1
                    break
    print(safe)

if __name__ == "__main__":
    main()