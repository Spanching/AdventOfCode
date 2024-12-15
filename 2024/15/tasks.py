def input():
    return "raw"

directions = {
    "<": -1+0j,
    ">": 1+0j,
    "^": -1j,
    "v": 1j
}
visualize = False

def print_warehouse(robot, walls, obstacles, n, m):
    if not visualize:
        return
    for j in range(n):
        for i in range(m):
            position = complex(i, j)
            if position in walls:
                print("#", end="")
            elif position in obstacles:
                print("O", end="")
            elif position == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()
    print()
    

def task1(puzzle_input: str) -> int:
    warehouse, moves = puzzle_input.split("\n\n")
    robot, walls, obstacles, n, m = create_level(warehouse)
    print_warehouse(robot, walls, obstacles, n, m)
    for line in moves:
        for d in line.strip():
            if visualize:
                print(f"Move {d}:")
            move = directions[d]
            new_pos = robot + move
            if new_pos in walls:
                continue
            elif new_pos in obstacles:
                while new_pos in obstacles:
                    new_pos += move
                if new_pos in walls:
                    continue
                else:
                    # move all boxes from start pos to new pos (exclusive)
                    robot += move
                    obstacles.remove(robot)
                    obstacles.append(new_pos)
            else:
                robot = new_pos
            print_warehouse(robot, walls, obstacles, n, m)
    output = sum(obstacles)
    output = int(output.real + 100*output.imag)
    return output

def create_level(warehouse):
    robot = None
    walls = []
    obstacles = []
    for j, line in enumerate(warehouse.split("\n")):
        for i, c in enumerate(line):
            if c == "#":
                walls.append(complex(i, j))
            elif c == "@":
                robot = complex(i, j)
            elif c == "O":
                obstacles.append(complex(i,j))
    n, m = j+1, i+1
    return robot,walls,obstacles,n,m

def create_double_level(warehouse):
    robot = None
    walls = []
    obstacles = []
    for j, line in enumerate(warehouse.split("\n")):
        for i, c in enumerate(line):
            if c == "#":
                walls.append(complex(i, j))
            elif c == "@":
                robot = complex(i, j)
            elif c == "O":
                obstacles.append(complex(i,j))
    n, m = j+1, i+1
    return robot,walls,obstacles,n,m

def task2(puzzle_input: str) -> int:
    warehouse, moves = puzzle_input.split("\n\n")
    robot, walls, obstacles, n, m = create_level(warehouse)
    
    print_warehouse(robot, walls, obstacles, n, m)
    for line in moves:
        for d in line.strip():
            if visualize:
                print(f"Move {d}:")
            move = directions[d]
            new_pos = robot + move
            if new_pos in walls:
                continue
            elif new_pos in obstacles:
                while new_pos in obstacles:
                    new_pos += move
                if new_pos in walls:
                    continue
                else:
                    # move all boxes from start pos to new pos (exclusive)
                    robot += move
                    obstacles.remove(robot)
                    obstacles.append(new_pos)
            else:
                robot = new_pos
            print_warehouse(robot, walls, obstacles, n, m)
    output = sum(obstacles)
    output = int(output.real + 100*output.imag)
    return output
