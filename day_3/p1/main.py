import re

def main():
    with open("../input.txt",'r') as f:
        output = f.read()
        matches = re.findall(r"mul\((\d+),(\d+)\)", output)
        result = 0
        for match in matches:
            num1, num2 = map(int, match)
            result += num1 * num2
        print(result)

if __name__ == "__main__":
    main()