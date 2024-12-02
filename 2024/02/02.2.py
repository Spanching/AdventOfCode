day = 2

all_lists = []
save = 0

with open(f"2024/{day:02d}/input", "r") as f:
    for line in f.readlines():
        l = []
        for level in line.split(" "):
            l.append(int(level))
        all_lists.append(l)


def calculate_levels(l):
    new = []
    for index, level in enumerate(l[:-1]):
        new.append(level - l[index + 1])
    return new
    

def check_list(l):
    for level in l:
        if level <= 0:
            return False
        if level > 3:
            return False
    return True

def check_list2(l):
    for level in l:
        if level >= 0:
            return False
        if level < -3:
            return False
    return True

def construct(levels, i):
    new = []
    if i == 0:
        return l[1:]
    if i == len(levels)-1:
        return l[:-1]
    for index, level in enumerate(l):
        if index == i:
            continue
        elif index == i:
            new.append(level+levels[i+1])
        else:
            new.append(level)
    return new

def negate_list(l):
    return [-x for x in l]

for l in all_lists:
    levels = calculate_levels(l)
    if check_list(levels) or check_list2(levels):
        save += 1
        continue
    for idx, level in enumerate(l):
        levels = calculate_levels(construct(l, idx))
        if check_list(levels) or check_list2(levels):
            save += 1
            break
    else:
        print(f"original: {l}")

print(save)