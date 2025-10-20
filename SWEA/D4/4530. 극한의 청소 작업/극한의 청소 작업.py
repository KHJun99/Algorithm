def count_4(n):
    count = 0
    length = 0
    n = abs(n)

    while n > 0:
        remain = n % 10
        n = n // 10
        if remain >= 4:
            count += (remain - 1) * (9 ** length)
        else:
            count += remain * (9 ** length)
        length += 1
    return count

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    a = count_4(A)
    b = count_4(B)

    if A < 0 < B :
        result = a + b - 1
    else:
        result = abs(b - a)

    print(f'#{tc} {result}')