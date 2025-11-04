# 백준_2573_빙산 (G4)
from collections import deque


def melting():
    global iceberg

    # 녹는 양을 먼저 계산 (동시에 녹아야 하므로)
    melt_amount = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if iceberg[r][c] > 0:
                cnt = 0
                for dx, dy in delta:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < N and 0 <= nc < M and iceberg[nr][nc] == 0:
                        cnt += 1
                melt_amount[r][c] = cnt

    # 계산된 양만큼 녹이기
    for r in range(N):
        for c in range(M):
            iceberg[r][c] = max(0, iceberg[r][c] - melt_amount[r][c])


def count_islands():
    visited = [[False] * M for _ in range(N)]
    island_cnt = 0

    for r in range(N):
        for c in range(M):
            if iceberg[r][c] > 0 and not visited[r][c]:
                # 새로운 섬 발견
                island_cnt += 1

                # BFS로 연결된 모든 빙산 탐색
                queue = deque([(r, c)])
                visited[r][c] = True

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

    return island_cnt


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

year = 0
while True:
    # 빙산의 개수 확인
    island_count = count_islands()

    # 빙산이 두 개 이상으로 분리
    if island_count >= 2:
        print(year)
        break

    # 빙산이 모두 녹았으면
    if island_count == 0:
        print(0)
        break

    # 1년 경과
    melting()
    year += 1
