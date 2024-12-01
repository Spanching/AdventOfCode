
l1, l2 = [], []

with open("2024/01/input", "r") as f:
    for line in f.readlines():
        one, two = line.split("   ")
        one, two = int(one), int(two)
        l1.append(one)
        l2.append(two)

l1.sort()
l2.sort()

print(l1)
print(l2)

total = 0
for i,j in zip(l1, l2):
    diff = abs(i-j)
    total += diff

print(total)