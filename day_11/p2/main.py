from math import floor, log10
from functools import lru_cache

@lru_cache(maxsize=None)
def blink(stone, blink_left):
    if blink_left == 0:
        return 1
    blink_left -= 1
    if stone == 0:
        return blink(1, blink_left)
    digits = floor(log10(stone)) + 1
    if digits % 2 == 0:
        left = stone // 10 ** (digits // 2)
        right = stone - left * 10 ** (digits // 2)
        return blink(left, blink_left) + blink(right, blink_left)
    return blink(stone * 2024, blink_left)

def main():
    file=open("../input.txt",'r')
    stones = [int(l) for l in file.read().split()]
    print(stones)
    result = sum(blink(stone, 75) for stone in stones)
    print(result)

if __name__ == "__main__":
    main()