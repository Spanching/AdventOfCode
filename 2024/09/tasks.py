
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

def extract_block(memory, mem_idx):
    rev_memory = memory[0:mem_idx+1][::-1]
    idx = 0
    data = rev_memory[idx]
    length = 0
    for d in rev_memory:
        if d == data:
            length += 1
        else:
            break
    return (data, length)

def extract_memory2(filesystem):
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

def remove_block(system, block, index):
    before = system[index-1]
    had_before = False
    if before[2] == -1:
        #space before -> append this one
        del system[index-1]
        system.insert(index-1, (before[0], block[1], -1))
        had_before = True
    if index != len(system)-1:
        # not last
        after = system[index+1]
        if after[2] == -1:
            # space after
            if had_before:
                del system[index-1]
                system.insert(index-1, (before[0], after[1], -1))
                del system[index+1]
            else:
                del system[index+1]
                system.insert(index+1, (block[0], after[1], -1))
    del system[index]

def find_block(system, length):
    for idx, block in enumerate(system[::-1]):
        if block[2] == -1:
            # is space
            continue
        if block[1]-block[0] <= length:
            remove_block(system, block, len(system)-1-idx)
            return block
    return None

def remove_space(system, space, block_length, index):
    if space[1]-space[0] == block_length:
        del system[index]
        return
    else:
        del system[index]
        system.insert(index, (space[0]+block_length, space[1], -1))

def find_space(system, length):
    for idx, space in enumerate(system):
        if space[2] == -1:
            # is space
            if space[1]-space[0] >= length:
                remove_space(system, space, length, idx)
                return space
    return None

def task2(puzzle_input: str) -> int:
    memory = extract_memory(puzzle_input)
    system = extract_memory2(puzzle_input)
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