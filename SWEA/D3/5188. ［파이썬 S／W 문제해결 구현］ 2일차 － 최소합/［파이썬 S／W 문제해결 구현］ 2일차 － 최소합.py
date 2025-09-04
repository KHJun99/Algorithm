def dfs(i, j, acc, n):
    """
    
    Args:
        i: 현재 위치 행 좌표
        j: 현재 위치 열 좌표
        acc: (0, 0)에서 (i, j)까지의 누적 합
        n: 보드 한 변 길이 (N)

    Returns: ans (글로벌 변수 수정)

    """
    global ans
    
    # 누적합이 이미 최적해(ans) 이상이면 더 내려가도 의미 없음
    if acc >= ans:
        return

    # 목적지 도달
    if i == n - 1 and j == n - 1:
        # acc는 현재 칸까지의 총합이므로 그대로 비교 / 갱신
        ans = min(ans, acc)
        return

    # 아래로 이동
    if i + 1 < n:
        # 다음 칸의 값을 누적해서 재귀 호출
        dfs(i + 1, j, acc + arr[i + 1][j], n)

    # 오른쪽으로 이동
    if j + 1 < n:
        # 다음 칸의 값을 누적해서 재귀 호출
        dfs(i, j + 1, acc + arr[i][j + 1], n)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')

    dfs(0, 0, arr[0][0], N)

    print(f'#{tc} {ans}')
