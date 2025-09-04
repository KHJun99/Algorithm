import sys
sys.setrecursionlimit(10_000)        # 재귀 최대 깊이 여유 있게 확보 (최대 100칸)

input = sys.stdin.readline

# [입력] 10줄 * 10칸 (0: 빈칸, 1: 덮어야 할 칸)
board = [list(map(int, input().split())) for _ in range(10)]

# [상태] 크기별 남은 색종이 수 (인덱스 1~5 사용, 0은 사용 안 함)
# 문제 조건: 각 크기 색종이 5장씩
left = [0, 5, 5, 5, 5, 5]

INF = 10**9
answer = INF  # 지금까지 발견한 최소 사용 수(정답). 더 작은 해를 찾을수록 갱신.

def find_next_one(bd):
    """
    아직 덮지 못한 '1' 중에서 가장 먼저 만나는 좌표를 반환한다.
    - 탐색 순서: (0,0) → (0,1) → ... → (0,9) → (1,0) → ... → (9,9)
    - 이유: 항상 '가장 왼쪽 위'부터 채우면, 분기(탐색 가지)가 줄어드는 효과가 있음
    - 반환값: (i, j) 또는 없으면 (-1, -1)
    """
    for i in range(10):
        for j in range(10):
            if bd[i][j] == 1:
                return i, j
    return -1, -1  # 더 이상 덮을 1이 없음 = 모든 칸을 성공적으로 덮음

def can_place(bd, x, y, size):
    """
    (x, y)를 좌상단으로 하는 size×size 색종이를 '붙일 수 있는지' 검사.
    조건:
      1) 보드 경계를 벗어나지 않을 것
      2) 해당 정사각형 영역의 모든 칸이 1일 것 (이미 0이면 덮으면 안 됨)
    """
    # [1] 범위 체크: x~x+size-1, y~y+size-1 이 0..9 안에 들어야 함
    if x + size > 10 or y + size > 10:
        return False
    # [2] 내용 체크: 모든 칸이 1이어야만 색종이를 올릴 수 있음
    for i in range(x, x + size):
        for j in range(y, y + size):
            if bd[i][j] != 1:
                return False
    return True

def place(bd, x, y, size, val):
    """
    (x, y) 시작 size×size 영역을 val(0 또는 1)로 채운다.
    - 백트래킹 핵심: '붙일 때는 0으로', '되돌릴 때는 1로' 복구.
    - 깊은 복사를 쓰지 않고 제자리 수정 + 복구를 하므로 메모리/시간 이득.
    """
    for i in range(x, x + size):
        for j in range(y, y + size):
            bd[i][j] = val

def dfs(used):
    """
    백트래킹(DFS)로 최소 장 수 탐색.
    매 호출의 의미:
      - 지금까지 'used' 장을 사용한 상태에서,
      - 다음으로 덮어야 할 '1'을 골라,
      - 붙일 수 있는 모든 색종이 크기를 시도해 본다.
    """
    global answer

    # [가지치기 1] 이미 현 최적(answer) 이상으로 사용했으면 더 볼 가치 없음
    if used >= answer:
        return

    # [다음 타겟] 아직 덮지 않은 '1' 중 가장 왼쪽 위
    x, y = find_next_one(board)

    # [종료 조건] 덮을 1이 더 이상 없으면 성공적으로 모든 1을 덮은 상태
    if x == -1:
        answer = min(answer, used)  # 최솟값 갱신
        return

    # [중요 휴리스틱] 큰 색종이부터 시도 (5 → 4 → 3 → 2 → 1)
    # 이유: 큰 걸 먼저 붙여서 넓은 영역을 빨리 덮으면 분기 수가 줄어드는 경향
    for size in range(5, 0, -1):
        # [가지치기 2] 해당 크기 색종이가 더 이상 남아있지 않은 경우 스킵
        if left[size] == 0:
            continue

        # [검사] (x,y) 위치에 해당 크기를 놓을 수 있는지
        if not can_place(board, x, y, size):
            continue

        # === [선택] 색종이 하나 붙이기 ===
        place(board, x, y, size, 0)    # 덮인 영역을 0으로 바꿔서 '덮었다' 표시
        left[size] -= 1                # 해당 크기 재고 1장 소모

        dfs(used + 1)                  # 다음 단계로 진행 (사용 장수 +1)

        # === [되돌리기] 탐색 후 상태 복구 ===
        left[size] += 1                # 재고 되돌리기
        place(board, x, y, size, 1)    # 덮었던 영역을 다시 1로 되돌림

# [탐색 시작] 0장 사용으로 시작
dfs(0)

# [출력] 답을 못 찾았으면 -1, 찾았으면 최소 장 수
print(-1 if answer == INF else answer)
