coordinate = [list(map(int, input().split())) for _ in range(4)]

grid = [[0] * 101 for _ in range(101)]
for a, b, c, d in coordinate:
    for i in range(a, c):
        for j in range(b, d):
            if grid[i][j] == 0:
                grid[i][j] = 1

temp = []
for row in grid:
    temp.append(sum(row))

print(sum(temp))