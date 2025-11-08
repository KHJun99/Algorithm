dwarf = [int(input()) for _ in range(9)]

total = sum(dwarf)
diff = total  - 100

found = False
fake1, fake2 = 0, 0
for i in range(9):
    if found:
        break

    for j in range(i + 1, 9):
        if dwarf[i] + dwarf[j] == diff:
            fake1, fake2 = i, j
            found = True
            break

real = []
for i in range(9):
    if i != fake1 and i != fake2:
        real.append(dwarf[i])

real.sort()
for height in real:
    print(height)

