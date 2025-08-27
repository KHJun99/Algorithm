from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * N for _ in range(N)]

house = []

# BFS
for r in range(N):
    for c in range(N):
        if grid[r][c] == '1' and not visited[r][c]:
            # 단지 시작
            q = deque([(r, c)])
            visited[r][c] = True
            cnt = 1

            while q:
                x, y = q.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and grid[nx][ny] == '1':
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cnt += 1

            house.append(cnt)

house.sort()
print(len(house))
for idx in house:
    print(idx)