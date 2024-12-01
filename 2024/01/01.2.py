
import os

l1, l2 = [], []

with open("2024/01/input", "r") as f:
    for line in f.readlines():
        one, two = line.split("   ")
        one, two = int(one), int(two)
        l1.append(one)
        l2.append(two)

total = 0
cache = {}

for i in l1:
    contained = 0
    if cache.get(i, -1) != -1:
        total += i * cache.get(i)
    else:
        for j in l2:
            if i == j:
                contained += 1
        cache[i] = contained
        total += (i * contained)

print(total)