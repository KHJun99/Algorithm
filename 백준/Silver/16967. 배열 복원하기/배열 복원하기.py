H, W, X, Y = map(int, input().split())

array_B = []
for _ in range(H + X):
    array = list(map(int, input().split()))
    array_B.append(array)

array_A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i < X or j < Y:
            # 겹치지 않은 부분
            array_A[i][j] = array_B[i][j]
        else:
            # 겹친 부분
            array_A[i][j] = array_B[i][j] - array_A[i - X][j - Y]

for row in array_A:
    print(*row)