N, M = map(int, input().split())

Basket = []

for x in range(N):
    Basket.append(x + 1)

for x in range(M):
    i, j = map(int, input().split())
    Basket[i-1:j] = reversed(Basket[i-1:j])

for x in Basket:
    print(x, end = " ")