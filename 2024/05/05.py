import functools


def create_comparator(rules):
    def comparator(a, b):
        if f"{a}|{b}" in rules:
            return -1
        return 1
    return comparator

def check_valid(program, rules):
    for i, p1 in enumerate(program):
        for j, p2 in enumerate(program[i:]):
            if f"{p2}|{p1}" in rules:
                return False
    return True

def task1(puzzle_input):
    rules = None
    programs = None
    for idx, line in enumerate(puzzle_input):
        if line == '':
            rules = puzzle_input[:idx]
            programs = list(map(lambda l: list(map(lambda i: int(i), l.split(","))), puzzle_input[idx+1:]))

    sum = 0
    for program in programs:
        if check_valid(program, rules):
            sum += program[int(len(program)/2)]
    return sum

def task2(puzzle_input):
    rules = None
    programs = None
    for idx, line in enumerate(puzzle_input):
        if line == '':
            rules = puzzle_input[:idx]
            programs = list(map(lambda l: list(map(lambda i: int(i), l.split(","))), puzzle_input[idx+1:]))

    sum = 0
    for idx, program in enumerate(programs):
        if check_valid(program, rules):
            continue
        program = sorted(program, key=functools.cmp_to_key(create_comparator(rules)))

        sum += program[len(program) // 2]
        
    return sum