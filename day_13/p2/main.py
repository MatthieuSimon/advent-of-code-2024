import re

def main():    
    with open("../input.txt") as file:
        data = []
        tokens = 0
        for line in file.readlines():
            if line == "\n":
                continue
            else:
                values = re.findall(r"\d+", line)
                data.append((int(values[0]), int(values[1])))
                if "Prize" in line:
                    num = ((10000000000000 + data[2][0]) * data[0][1]) - ((10000000000000 + data[2][1]) * data[0][0])
                    denom = (data[1][0] * data[0][1]) - (data[1][1] * data[0][0])
                    if num % denom == 0:
                        y = int(num / denom)
                        x = 0
                        if ((10000000000000 + data[2][0]) - (data[1][0] * y)) % data[0][0] == 0:
                            x = int(((10000000000000 + data[2][0]) - (data[1][0] * y)) / data[0][0])
                        if x != 0:
                            tokens += 3 * x + y
                    data = []
    print(tokens)
    
if __name__ == "__main__":
    main()