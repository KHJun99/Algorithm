
def dfs(x, y):
    # 범위 밖이거나, 벽이거나, 이미 방문한 경우
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if maze[x][y] == 1 or visited[x][y]:
        return False
    
    # 도착 지점이면 True 반환
    if maze[x][y] == 3:
        return True

    visited[x][y] = True  # 방문 처리

    # 상, 하, 좌, 우 탐색
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if dfs(x+dx, y+dy):
            return True

    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input().strip()))) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 시작 위치 찾기
    start_x = start_y = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    if dfs(start_x, start_y):
        result = 1
    else:
        result = 0
    print(f"#{tc} {result}")
