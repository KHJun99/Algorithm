import sys
sys.setrecursionlimit(10**6)


def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for idx in range(4):
        nr, nc = r + dr[idx], c + dc[idx]

        if 0 <= nr < N and 0 <= nc < M and zido[r][c] > zido[nr][nc]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]


N, M = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = dfs(0, 0)

print(result)