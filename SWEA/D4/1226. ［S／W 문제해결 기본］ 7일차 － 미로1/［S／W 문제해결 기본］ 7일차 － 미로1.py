from collections import deque


def find_maze(sx, sy, maze):
    N = len(maze)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy

            # 1) 경계 체크
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 2) 벽(1)은 통과 불가
            if maze[nx][ny] == 1:
                continue
            # 3) 이미 방문했으면 패스
            if visited[nx][ny]:
                continue

            # 4) 목표(3) 도달
            if maze[nx][ny] == 3:
                return 1

            # 5) 길(0) 혹은 시작(2)라면 큐에 추가
            visited[nx][ny] = True
            q.append((nx, ny))

    return 0


T = 10
for _ in range(T):
    tc = int(input())

    # 16줄을 읽되, 공백 유무에 상관없이 파싱되게 처리
    maze = []
    for _ in range(16):
        line = input().strip()
        if ' ' in line:
            row = list(map(int, line.split()))
        else:
            row = list(map(int, line))  # '010201...' 형태
        maze.append(row)

    # 시작점(2) 찾기
    sx = sy = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sx, sy = i, j
                break

    result = find_maze(sx, sy, maze)
    print(f'#{tc} {result}')
