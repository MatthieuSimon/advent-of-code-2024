import re

def calculate_values(target, intermediate_result, test_values):
    if not test_values:
        return intermediate_result == target
    next_value, *test_values = test_values
    return calculate_values(target, intermediate_result + next_value, test_values) or calculate_values(target, intermediate_result * next_value, test_values) or calculate_values(target, int(str(intermediate_result) + str(next_value)), test_values)

def main():
    with open("../input.txt", 'r') as file:
        result = 0
        row = file.readlines()
        for line in row:
            target, *test_values = map(int, re.findall(r"\d+", line))
            if calculate_values(target, test_values[0], test_values[1:]):
                result += target
        print(result)

if __name__ == "__main__":
    main()