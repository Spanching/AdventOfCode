
directions=[(0,-1), (-1,0), (1,0), (0, 1)]
visited = []
visiting = (0,0)
printing = False

def input():
    return "intlist"

def get_heads(trailmap: list[int]) -> list[tuple[int]]:
    heads = []
    for i, line in enumerate(trailmap):
        for j, c in enumerate(line):
            if c == 0:
                heads.append((i,j))
    return heads

def depth_first_search(trailmap: list[int], head: tuple[int], n, m, ignore_visited = False):
    global visiting
    global visited
    visited.append(head)
    output = 0
    visiting = head
    if printing:
        print_trailmap(trailmap)
    value = trailmap[head[0]][head[1]]
    for direction in directions:
        next = (head[0]+direction[0], head[1]+direction[1])
        if not ignore_visited and next in visited:
            continue
        if next[0] < 0 or next[0] > n or next[1] < 0 or next[1] > m:
            continue
        if trailmap[next[0]][next[1]] == value+1:
            if value+1 == 9:
                visited.append(next)
                output += 1
                continue
            output += depth_first_search(trailmap, next, n, m, ignore_visited=ignore_visited)
    return output

def print_trailmap(trailmap):
    for i, line in enumerate(trailmap):
        for j, n in enumerate(line):
            if (i,j) == visiting:
                print("\033[94mX\033[0m", end="")
            elif (i,j) in visited:
                print(f"\033[96m{n}\033[0m", end="")
            else:
                print(n, end="")
        print()
    print()

def task1(trailmap: list[int]) -> int:
    global visited
    heads = get_heads(trailmap)
    n, m = len(trailmap)-1, len(trailmap[0])-1
    sum = 0
    for head in heads:
        # depth first search bc it rocks
        visited = []
        sum += depth_first_search(trailmap, head, n, m)
    return sum

def task2(trailmap: list[int]) -> int:
    global visited
    heads = get_heads(trailmap)
    n, m = len(trailmap)-1, len(trailmap[0])-1
    sum = 0
    for head in heads:
        # depth first search bc it rocks
        visited = []
        sum += depth_first_search(trailmap, head, n, m, ignore_visited=True)
    return sum
