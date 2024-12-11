from collections import defaultdict
from tqdm import tqdm
from bisect import insort, bisect

def input():
    return "int"

max_depth = 75


def full_blink(configuration: list[int]):
    new_list = []
    for index, number in enumerate(configuration):
        if number == 0:
            new_list.append(1)
            continue
        num_str = str(number)
        if len(num_str) % 2 == 0:
            first = int(num_str[:len(num_str)//2])
            second = int(num_str[len(num_str)//2:])
            new_list.append(first)
            new_list.append(second)
        else:
            new_list.append(configuration[index] * 2024)
    return new_list

blink_memo = defaultdict(list)
def blink(number) -> list[int]:
    if blink_memo[number]:
        return blink_memo[number]
    if number == 0:
        return [1]
    num_str = str(number)
    if len(num_str) % 2 == 0:
        first = int(num_str[:len(num_str)//2])
        second = int(num_str[len(num_str)//2:])
        blink_memo[number] = [first, second]
        return [first, second]
    else:
        blink_memo[number] = [number * 2024]
        return [number * 2024]

value_memo = {}
def value(number: int, depth: int) -> int:
    if depth == 0:
        return 1
    if (number, depth) in value_memo:
        return value_memo[(number, depth)]
    output = 0
    for new_number in blink(number):
        value_memo[(new_number, depth-1)] = value(new_number, depth-1)
        output += value_memo[(new_number, depth-1)]
    value_memo[(number, depth)] = output
    return output

def task1(puzzle_input: list[int]) -> int:
    output = puzzle_input
    for _ in range(25):
        output = full_blink(output)
    return len(output)

def task2(puzzle_input: list[int]) -> int:
    sum = 0
    for number in puzzle_input:
        sum += value(number, max_depth)
    return sum
