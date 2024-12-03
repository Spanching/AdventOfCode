import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import util.input as util

day = 4
sample = True
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input_list = util.get_input_as_line_list(path)

print(input_list)