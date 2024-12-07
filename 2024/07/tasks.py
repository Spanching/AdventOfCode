
values = []

def new_val(first, second, op):
    new_value = 0
    match op:
        case "+": new_value = first + second
        case "*": new_value = first * second
        case "|": new_value = int(str(first) + str(second))
    return new_value

def valid_1(result: int, input: list[int]):
    intermediate = input[0]
    possibilities = {
        "": intermediate
    }
    for number in input[1:]:
        keys = list.copy(list(possibilities.keys()))
        while len(keys) > 0:
            key = keys.pop(0)
            for op in ["+", "*"]:
                new_value = new_val(possibilities[key], number, op)
                if new_value > result:
                    continue
                possibilities[key + op] = new_value
            del possibilities[key]
    return result in [v for k,v in possibilities.items() if len(k)==len(input)-1]

def task1(puzzle_input: list[str]) -> int:
    sum = 0
    for line in puzzle_input:
        args = line.split(" ")
        test_value = args.pop(0)
        test_value = int(test_value[:len(test_value)-1])
        input_values = list(map(lambda a: int(a), args))
        if valid_1(test_value, input_values):
            sum += test_value
    return sum

def valid(result: int, input: list[int]):
    intermediate = input[0]
    possibilities = [intermediate]
    for number in input[1:]:
        keys = possibilities
        possibilities = []
        while len(keys) > 0:
            value = keys.pop(0)
            for op in ["+", "*", "|"]:
                new_value = new_val(value, number, op)
                if new_value > result:
                    continue
                possibilities.append(new_value)
    return result in possibilities


def task2(puzzle_input: list[str]) -> int:
    sum = 0
    for line in puzzle_input:
        args = line.split(" ")
        test_value = args.pop(0)
        test_value = int(test_value[:len(test_value)-1])
        input_values = list(map(lambda a: int(a), args))
        if valid(test_value, input_values):
            sum += test_value
    return sum
