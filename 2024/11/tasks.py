def input():
    return "int"

def blink(configuration: list[int]):
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

def task1(puzzle_input: list[int]) -> int:
    output = puzzle_input
    for _ in range(25):
        output = blink(output)
    return len(output)

def task2(puzzle_input: list[int]) -> int:
    output = puzzle_input
    for _ in range(75):
        output = blink(output)
    return len(output)
