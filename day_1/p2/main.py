def main():
    file=open("../input.txt",'r') 
    row = file.readlines()
    left_culumn, right_column = [], []
    for line in row:
        list_line = line.split()
        left_culumn.append(list_line[0])
        right_column.append(list_line[1])
    similarity = 0
    for i in range(len(left_culumn)):
        similarity  += right_column.count(left_culumn[i]) * int(left_culumn[i])
    print(similarity)


if __name__ == "__main__":
    main()