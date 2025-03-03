N, M = map(int, input().split())

A, B = [], []

# 행렬 A 입력
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A와 B의 합 계산 및 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()     # 각 행의 끝에 줄 바꿈 추가
