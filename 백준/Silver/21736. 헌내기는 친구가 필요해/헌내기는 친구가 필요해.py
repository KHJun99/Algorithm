from collections import deque


def bfs():
    global result

    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[False] * M for _ in range(N)]

    q = deque()
    for r in range(N):
        for c in range(M):
            if zido[r][c] == 'I':
                q.append((r, c))
            if zido[r][c] == 'X':
                visited[r][c] = True

    while q:
        x, y = q.popleft()

        visited[x][y] = True
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if zido[nx][ny] == 'P':
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        result += 1
                    if zido[nx][ny] == 'O':
                        visited[nx][ny] = True
                        q.append((nx, ny))


N, M = map(int, input().split())
zido = [input() for _ in range(N)]
result = 0

bfs()

print(result if result > 0 else 'TT')