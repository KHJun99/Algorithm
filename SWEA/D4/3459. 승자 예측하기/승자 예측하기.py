T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    while N > 3:
        N = N // 2 + 1
        N = N // 2 - 1

    if N >= 2 or N == 0:
        winner = 'Alice'
    else:
        winner = 'Bob'

    print(f'#{tc} {winner}')
