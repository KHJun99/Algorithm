N, M = map(int, input().split())

Basket = [0] * N

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i,j+1):
        Basket[y-1] = k

for x in range(N):
    print(Basket[x], end=" ")