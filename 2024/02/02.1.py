day = 2

all_lists = []
save = 0

with open(f"2024/{day:02d}/input", "r") as f:
    for line in f.readlines():
        l = []
        for level in line.split(" "):
            l.append(int(level))
        all_lists.append(l)

for l in all_lists:
    for index, level in enumerate(l[:-1]):
        l[index] = level - l[index + 1]
    del l[-1]

for l in all_lists:
    # print(l)
    first = l[0]
    if first < 0 and first > -4:
        for idx, level in enumerate(l):
            if level >= 0:
                break
            if level < 0 and level > -4:
                if idx == len(l) - 1:
                    print(l)
                    save += 1
            else:
                break
    elif first > 0 and first < 4:
        for idx, level in enumerate(l):
            if level <= 0:
                break
            if level > 0 and level < 4:
                if idx == len(l) - 1:
                    print(l)
                    save += 1
            else:
                break

print(save)