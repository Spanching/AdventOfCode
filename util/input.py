from typing import List


def get_input_as_line_list(input_path: str) -> List[str]:
    output = []
    with open(input_path, "r") as f:
        for line in f.readlines():
            output.append(line.strip())
    return output

def get_input_as_raw_string(input_path: str) -> str:
    output = ""
    with open(input_path, "r") as f:
        for line in f.readlines():
            output += line
    return output

def get_input_as_one_line_string(input_path: str) -> str:
    output = ""
    with open(input_path, "r") as f:
        for line in f.readlines():
            output += line.strip()
    return output