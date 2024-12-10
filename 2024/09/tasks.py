
def input():
    return "oneline"

def extract_memory(filesystem):
    memory = []
    for idx, amount in enumerate(filesystem):
        if idx % 2 == 1:
            memory += ["."] * int(amount)
            continue
        memory += [str(idx//2)] * int(amount)
    return memory

def task1(puzzle_input: str) -> int:
    memory = extract_memory(puzzle_input)
    free_spaces = []
    last_data = "."
    for idx, data in enumerate(memory):
        if data == ".":
            free_spaces.append(idx)
    for idx, data in enumerate(memory):
        if data == ".":
            continue
        if len(free_spaces) == 0:
            break
        last_data = memory.pop()
        while last_data == ".":
            last_data = memory.pop()
        if free_spaces:
            first_free_space = free_spaces.pop(0)
            if first_free_space > len(memory) - 1:
                memory.append(last_data)
            else:
                memory[first_free_space] = last_data
        else:
            break
    sum = 0
    for idx, data in enumerate(memory):
        if data == ".":
            break
        sum += int(data) * idx
    return sum

def extract_system(filesystem):
    system = []
    fs_idx = 0
    for idx, amount in enumerate(filesystem):
        if int(amount) == 0:
            continue
        if idx % 2 == 1:
            system.append((fs_idx, fs_idx+int(amount), -1))
            fs_idx += int(amount)
            continue
        system.append((fs_idx, fs_idx+int(amount), idx//2))
        fs_idx += int(amount)
    return system

def checksum(system):
    sum = 0
    for b, e, n in system:
        if n == -1:
            continue
        for i in range(e-b):
            sum += (b+i)*n
    return sum

def task2(puzzle_input: str) -> int:
    system = extract_system(puzzle_input)
    result = []
    while system:
        first = system[0]
        last = system[-1]
        if first[2] != -1:
            del system[0]
            result.append(first)
            continue
        if last[2] == -1:
            del system[-1]
            result.append(last)
            continue
        # first is space
        # last is file
        for index, space in enumerate(system):
            if space[2] != -1:
                continue
            space_length = space[1] - space[0]
            last_length = last[1] - last[0]
            if space_length >= last_length:
                new_file = (space[0], space[0]+last_length, last[2])
                if space_length == last_length:
                    del system[index]
                    system.insert(index, new_file)
                    del system[-1]
                else:
                    new_space = (new_file[1], space[1], -1)
                    del system[index]
                    system.insert(index, new_space)
                    system.insert(index, new_file)
                    del system[-1]
                    system.append((last[0], last[1], -1))
                break
        else:
            result.append(last)
            del system[-1]
            pass
    return checksum(result)