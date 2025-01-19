N, X = map(int, input().split())

Array = list(map(int, input().split()))

for i in range(N):
    if Array[i] < X:
        print(Array[i], end = " ")