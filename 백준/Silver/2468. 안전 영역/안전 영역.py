from collections import deque


def find_height():
    tmp_height = set()

    for r in range(N):
        for c in range(N):
            tmp_height.add(region[r][c])

    return list(tmp_height)


def check_region(h_lst):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_safe_region = float('-inf')

    for high in h_lst:
        visited = [[False] * N for _ in range(N)]
        queue = deque()
        ground = 0

        for r in range(N):
            for c in range(N):
                if region[r][c] <= high:
                    visited[r][c] = True

        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    visited[r][c] = True
                    queue.append((r, c))

                    while queue:
                        cx, cy = queue.popleft()

                        for idx in range(4):
                            nx, ny = cx + dx[idx], cy + dy[idx]
                            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                    ground += 1

        if ground > max_safe_region:
            max_safe_region = ground

    return max_safe_region


N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

height = [0] + find_height()

result = check_region(height)

print(result)