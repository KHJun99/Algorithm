# import sys
import copy
# sys.stdin = open('input.txt', 'r')
from collections import deque


def find_virus():
    """
    현재 격자(virus)에서 바이러스(값=2)의 좌표를 전부 찾아 리스트로 반환한다.
    반환 형식: [(r1, c1), (r2, c2), ...]
    """
    virus_coordinate = []
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                virus_coordinate.append((i, j))

    return virus_coordinate


# 벽을 세우는 재귀 함수
def make_wall(cnt):
    """
    cnt : 세운 벽의 수
        - 벽을 3개 세우면 bfs()로 감염을 시뮬레이션하여 ans 갱신 후 반환
        - 그렇지 않으면 모든 칸ㄴ을 순회하면 빈 칸(0)에 벽(1)을 세우고 재귀적으로 진행
    """
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:        # 빈 칸이면
                virus[i][j] = 1         # 벽 세우기
                make_wall(cnt + 1)      # 다음 벽 세우기
                virus[i][j] = 0         # 백트래킹


def bfs():
    queue = deque()
    tmp_virus = copy.deepcopy(virus)
    queue.extend(coordinate)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이면 스킵
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 인접한 칸이 빈 칸(0)이면 감염(2) 시키고 큐에 삽입
            if tmp_virus[nx][ny] == 0:
                tmp_virus[nx][ny] = 2
                queue.append((nx, ny))

    # 감연 종료 후 안전영역(0) 계산
    global ans
    cnt = 0

    for i in range(N):
        cnt += tmp_virus[i].count(0)

    # 최대값 갱신
    ans = max(ans, cnt)


# T = int(input())
# for tc in range(1, T + 1):
N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 초기 바이러스 좌표 목록
coordinate = find_virus()

# 최대 안전영역 크기
ans = 0
    
# 벽 3개 세우기
make_wall(0)
print(ans)