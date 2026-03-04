N, S, M = map(int, input().split())

V = list(map(int, input().split()))

vol = [[0] * (M + 1) for _ in range(N + 1)]

vol[0][S] = 1

for i in range(N):
    for j in range(M + 1):
        if vol[i][j] == 1:
            min_vol = j - V[i]
            max_vol = j + V[i]

            if min_vol >= 0:
                vol[i + 1][min_vol] = 1

            if max_vol <= M:
                vol[i + 1][max_vol] = 1

result = -1

for i in range(M, -1, -1):
    if vol[N][i] == 1:
        result = i
        break

print(result)
