import sys
sys.path.append("c:/Users/AndreasK/Projects/AdventOfCode")

import util.input as util
import re
day = 4
sample = False
path = f"2024/{day:02d}/{'sample_' if sample else ''}input"

input_list = util.get_input_as_line_list(path)

output = 0
for i, list in enumerate(input_list):
    for j, char in enumerate(list):
        if i == 0 or i == len(input_list) - 1 or j == 0 or j == len(input_list) - 1:
            continue
        if char == "A":
            word1 = input_list[i-1][j-1] + "A" + input_list[i+1][j+1]
            word2 = input_list[i-1][j+1] + "A" + input_list[i+1][j-1]
            if (word1 == "SAM" or word1 == "MAS") and (word2 == "SAM" or word2 == "MAS"):
                output += 1
print(output)