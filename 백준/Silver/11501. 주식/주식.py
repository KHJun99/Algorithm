# 이익을 구하는 함수
def stock(lst):
    global N
    # lst의 마지막 인덱스를 최대값으로 가정
    max_price = lst[N - 1]
    price = 0

    for idx in range(N - 1, -1, -1):
        # max_price보다 리스트값이 작으면 이익 발생
        if max_price > lst[idx]:
            diff = max_price - lst[idx]
            price += diff
        # 이익이 발생할 수 없으므로 최대값 갱신
        else:
            max_price = lst[idx]

    return price


T = int(input())

for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    total = stock(prices)
    print(total)
