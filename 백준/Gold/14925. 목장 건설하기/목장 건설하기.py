# 백준_14925_목장_건설하기 (G4)
"""
## [문제 정리]
- 랜드씨가 소개받은 땅은 직사각형
    - 대부분 들판이지만, 여기저기 베기 어려운 나무와 치울 수 없는 바위 존재
- 목장을 하나의 정사각형으로 최대한 크게 지으려고 한다.
    - 단, 그 안에 나무나 바위는 없어야 한다.
- 땅의 세로 길이가 M미터, 가로가 N미터 일 때, 1미터 간격으로 격자로 된 땅의 지도를 M x N 행렬로 표현
- 행렬의 원소 0 : 들판
- 행렬의 원소 1 : 나무
- 행렬의 원소 2 : 돌
- 랜드씨의 땅에서 지을 수 있는 가장 큰 정사각현 목장의 한 변의 크기 L을 출력하시오.
"""
M, N = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(M)]

for i in range(N):
    if fields[0][i] == 0:
        dp[0][i] = 1
    else:
        dp[0][i] = 0

for j in range(M):
    if fields[j][0] == 0:
        dp[j][0] = 1
    else:
        dp[j][0] = 0

for i in range(1, M):
    for j in range(1, N):
        if fields[i][j] == 0:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

ans = 0
for r in range(M):
    for c in range(N):
        if ans < dp[r][c]:
            ans = dp[r][c]

print(ans)