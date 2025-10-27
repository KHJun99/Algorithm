# 카데인 알고리즘 사용
def kadane_1d(arr):
    # 1차원 최대 연속 부분합 (모두 음수여도 동작)
    best = cur = arr[0]
    for i in range(1, len(arr)):
        x = arr[i]
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

NEG_INF = -10**18
ans = NEG_INF

# 행 압축 + 1D 카데인
for top in range(N):
    col_sum = [0] * M  # top이 바뀔 때마다 초기화
    for bottom in range(top, N):
        # top..bottom 사이 행들을 열별로 누적
        for c in range(M):
            col_sum[c] += A[bottom][c]
        # 누적된 열합 배열에서 최대 연속 부분합
        ans = max(ans, kadane_1d(col_sum))

print(ans)