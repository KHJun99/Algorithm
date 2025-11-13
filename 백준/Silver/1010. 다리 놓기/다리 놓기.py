def combination(n, r):
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    # 초기값 : nC0 = 1
    for i in range(n + 1):
        dp[i][0] = 1

    # 파스칼 삼각형 : dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]


T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())

    result.append(combination(M, N))

for row in result:
    print(row)