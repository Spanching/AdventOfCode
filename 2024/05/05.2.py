import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import util.input as util

day = 5
sample = False
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input_list = util.get_input_as_line_list(path)

rules = None
programs = None
for idx, line in enumerate(input_list):
    if line == '':
        rules = input_list[:idx]
        programs = list(map(lambda l: list(map(lambda i: int(i), l.split(","))), input_list[idx+1:]))

valid_programs = []
after_rules = {}
before_rules = {}
for rule in rules:
    before, after = (int(rule.split("|")[0]), int(rule.split("|")[1]))
    if before in after_rules:
        after_rules[before].append(after)
    else:
        after_rules[before] = [after]
    if after in before_rules:
        before_rules[after].append(before)
    else:
        before_rules[after] = [before]
    
# print("Before:")
# print(before_rules)
# print("After:")
# print(after_rules)

sum = 0
def check_valid(idx, program, program_number):
    valid = True
    if program_number in after_rules:
        for after in after_rules[program_number]:
            if after in program[:idx]:
                    # print(f"{program_number} must be after {after}, but program is {program}")
                valid = False
                break
    if program_number in before_rules:
        for before in before_rules[program_number]:
            if idx != len(program) - 1 and before in program[idx+1:]:
                    # print(f"{program_number} must be before {before}, but program is {program}")
                valid = False
                break
    return valid

def correct_program(idx, program, program_number):
    if program_number in after_rules:
        for after in after_rules[program_number]:
            if after in program[:idx]:
                    # print(f"{program_number} must be after {after}, but program is {program}")
                program[program.index(after)] = program_number
                program[idx] = after
                correct_program(idx, program, after)
                    # valid = False
                    # break
    if program_number in before_rules:
        for before in before_rules[program_number]:
            if idx != len(program) - 1 and before in program[idx+1:]:
                program[program.index(before)] = program_number
                program[idx] = before
                correct_program(program.index(before), program, before)
                    # print(f"{program_number} must be before {before}, but program is {program}")
                # valid = False
                # break

for idx, program in enumerate(programs):
    # print(f"Program {idx}")
    valid = True
    for idx, program_number in enumerate(program):
        correct_program(idx, program, program_number)
    
    for idx, program_number in enumerate(program):
        valid = check_valid(idx, program, program_number)

    if not valid:
        print("ERROR")
    
print(sum)