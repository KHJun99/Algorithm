N = int(input())
notes = input().strip()

# 북동남서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0 # 초기 위치 
dir = 2     # 남쪽을 보고 있기 때문

xs, ys = [0], [0]

for note in notes:
    if note == 'L':
        dir = (dir - 1) % 4
    elif note == 'R':
        dir = (dir + 1) % 4
    else:
        x += dx[dir]
        y += dy[dir]
        xs.append(x)
        ys.append(y)

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

rows = max_x - min_x + 1
cols = max_y - min_y + 1
zido = [['#'] * cols for _ in range(rows)]

x, y = 0, 0
dir = 2

# 초기 위치
zido[x - min_x][y - min_y] = '.'

for note in notes:
    if note == 'L':
        dir = (dir - 1) % 4
    elif note == 'R':
        dir = (dir + 1) % 4
    else:
        x += dx[dir]
        y += dy[dir]
        zido[x - min_x][y - min_y] = '.'

for row in zido:
    print(''.join(row))