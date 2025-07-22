import sys
sys.setrecursionlimit(10000)

def draw_star(x, y, n):
    if n == 1:
        stars[x][y] = '*'
        return
    size = n // 3
    for i in range(3):
        for j in range(3):
            # 가운데(1,1)는 공백
            if i == 1 and j == 1:
                continue
            draw_star(x + i * size, y + j * size, size)

n = int(sys.stdin.readline())
stars = [[' ' for _ in range(n)] for _ in range(n)]

draw_star(0, 0, n)

# 출력
for row in stars:
    print(''.join(row))
