
import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import re

import util.input as util


day = 3
sample = False
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input_list = util.get_input_as_line_list(path)

output = 0
for line in input_list:
    matchings = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)
    for matching in matchings:
        nums = re.match("mul\((\d{1,3}),(\d{1,3})\)", matching)
        one, two = int(nums.group(1)), int(nums.group(2))
        output += one*two

print(output)
# 161289189