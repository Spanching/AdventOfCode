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

def insert_into_master(programs_before, program, master: list):
    index = 0
    for existing in master:
        if existing in programs_before:
            index = master.index(existing) + 1
    master.insert(index, program)
    if not check_valid(master):
        pass

def check_valid(program, printing = True):
    valid = True
    for idx, program_number in enumerate(program):
        if program_number in after_rules:
            for after in after_rules[program_number]:
                if after in program[:idx]:
                    if printing:
                        print(f"{after} must be after {program_number}, but program is {program}")
                    valid = False
                    break
        if program_number in before_rules:
            for before in before_rules[program_number]:
                if idx != len(program) - 1 and before in program[idx+1:]:
                    if printing:
                        print(f"{before} must be before {program_number}, but program is {program}")
                    valid = False
                    break
    return valid

def create_new(program):
    master_list = []
    for entry in program:
        if entry in before_rules:
            insert_into_master(before_rules[entry], entry, master_list)
        else:
            master_list.insert(0, entry)
        if not check_valid(master_list):
            pass
    return master_list
sum = 0

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
    if check_valid(program, False):
        continue
    new_program = create_new(program)
    # print(f"Program {new_program}")
    valid = check_valid(new_program)

    sum += new_program[int(len(new_program)/2)]

    if not valid:
        print("ERROR")
    
print(sum)