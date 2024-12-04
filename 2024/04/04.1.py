import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import util.input as util
import re
day = 4
sample = False
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input_list = util.get_input_as_line_list(path)

print(input_list)

def reverse(input_list):
    reversed_list = []
    for input in input_list:
        reversed_list.append(input[-1::-1])
    return reversed_list

def verticalize(input_list):
    vertical_list = []
    for _ in range(len(input_list[0])):
        vertical_list.append([])
    # make permutations
    for i, input in enumerate(input_list):
        for j, char in enumerate(input):
            vertical_list[j].append(char)
    output = []
    for char_list in vertical_list:
        output.append("".join(char_list))
    return output

def diagonalize(input_list):
    diag_ltr_list = []
    for i in range(len(input_list) + len(input_list[0]) - 1):
        diag_ltr_list.append([])
    for i, input in enumerate(input_list):
        for j, char in enumerate(input.strip()):
            idx = j - i + len(input_list) - 1
            diag_ltr_list[idx].append(char)
    output = []
    for char_list in diag_ltr_list:
        output.append("".join(char_list))
    return output

l1 = list.copy(input_list)
l2 = verticalize(input_list)
l3 = diagonalize(input_list)
l4 = diagonalize(reverse(list.copy(input_list)))
l5 = reverse(l1)
l6 = reverse(l2)
l7 = reverse(l3)
l8 = reverse(l4)

all_lists = [l1, l2, l3, l4, l5, l6, l7, l8]
print(all_lists)
output = 0
for list in all_lists:
    for l in list:
        output += len(re.findall("XMAS", l))
print(output)