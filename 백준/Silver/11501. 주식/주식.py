def stock(lst):
    global N
    max_price = lst[N - 1]
    price = 0

    for idx in range(N - 1, -1, -1):
        if max_price > lst[idx]:
            diff = max_price - lst[idx]
            price += diff
        else:
            max_price = lst[idx]

    return price


T = int(input())

for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    total = stock(prices)
    print(total)
