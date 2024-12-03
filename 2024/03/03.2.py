
import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import util.input as util
import re

day = 3
sample = False
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input = util.get_input_as_one_line_string(path)

output = 0
enable = True
for command in re.findall("don't\(\)|do\(\)|mul\(\d*,\d*\)", input):
    match command:
        case "do()": enable = True
        case "don't()": enable = False
        case _:
            if enable:
                nums = re.match("mul\((\d{1,3}),(\d{1,3})\)", command)
                one, two = int(nums.group(1)), int(nums.group(2))
                output += one * two

print(output)