from collections import deque
import sys
input = sys.stdin.readline

def fill_house():
    global visited, zido
    q = deque([(0, 0)])
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= M and not visited[nx][ny] and zido[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny))

    for i in range(N + 1):
        for j in range(M + 1):
            if visited[i][j] == False and zido[i][j] != 1:
                zido[i][j] = 1


def prefix_sum():
    ps = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        hap = 0
        for j in range(1, M + 1):
            hap += zido[i][j]
            ps[i][j] = ps[i-1][j] + hap
    return ps

def ps_sum(ps, a, b, c, d):
    return ps[c][d] - ps[a-1][d] - ps[c][b-1] + ps[a-1][b-1]

N, M = map(int, input().split())
zido = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(input())
    for j in range(1, M + 1):
        zido[i][j] = int(row[j - 1])

Q = int(input())
visited = [[False] * (M + 1) for _ in range(N + 1)]

fill_house()

ps = prefix_sum()

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    result = ps_sum(ps, r1, c1, r2, c2)

    if result == 0:
        print('Yes')
    else:
        print(f'No {result}')