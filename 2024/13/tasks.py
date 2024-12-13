import re

from tqdm import tqdm 

def input():
    return "raw"

a_reg = "Button A: X\+(\d*), Y\+(\d*)"
b_reg = "Button B: X\+(\d*), Y\+(\d*)"
p_reg = "Prize: X=(\d*), Y=(\d*)"

def task1(puzzle_input: str) -> int:
    machines = create_machines(puzzle_input)
    sum = 0
    for ((ax, ay), (bx, by), (px, py)) in machines:
        for i in range(101):
            for j in range(101):
                if ax*i + bx*j == px:
                    if ay*i + by*j == py:
                        sum += i*3+j
    return sum

def create_machines(puzzle_input, prize_offset=0):
    machine_input = [machine for machine in puzzle_input.split("\n\n")]
    machines = []
    for machine in machine_input:
        lines = machine.split("\n")
        btn_a = tuple(map(lambda i: int(i), re.match(a_reg, lines[0]).groups()))
        btn_b = tuple(map(lambda i: int(i), re.match(b_reg, lines[1]).groups()))
        prize = tuple(map(lambda i: int(i)+prize_offset, re.match(p_reg, lines[2]).groups()))
        machines.append((btn_a, btn_b, prize))
    return machines

def task2(puzzle_input: list[str]) -> int:
    machines = create_machines(puzzle_input, 10000000000000)
    sum = 0
    for ((ax, ay), (bx, by), (px, py)) in machines:
        i = (px*by-bx*py)/(ax*by-bx*ay)
        j = (py-ay*i)/by
        if i.is_integer() and j.is_integer():
            sum += i*3 + j
    return int(sum)
