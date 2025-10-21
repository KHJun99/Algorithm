g, s = map(int, input().split())

cnt = int(input())

garo = [0, g]
sero = [0, s]

for _ in range(cnt):
    dir, idx = map(int, input().split())

    if dir == 0:
        sero.append(idx)
    else:
        garo.append(idx)

garo.sort()
sero.sort()

max_g = 0
i = 0
while i < len(garo) - 1:
    width = garo[i + 1] - garo[i]
    if width > max_g:
        max_g = width

    i += 1

max_s = 0
j = 0
while j < len(sero) - 1:
    height = sero[j + 1] - sero[j]
    if height > max_s:
        max_s = height

    j += 1

print(max_g * max_s)

