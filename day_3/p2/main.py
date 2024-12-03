import re

def main():
    with open("../input.txt",'r') as f:
        output = f.read()
        matches = re.finditer(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)", output)
        result = 0
        do = True
        for match in matches:
            print(match)
            if match.group(1) and match.group(2) and do:
                num1, num2 = int(match.group(1)), int(match.group(2))
                result += num1 * num2
            elif match.group(0) == "don't()":
                do = False
            elif match.group(0) == "do()":
                do = True
        print(result)

if __name__ == "__main__":
    main()