def convert(s, n):
    global switch
    # 남학생일 경우
    if s == 1:
        for idx in range(1, N + 1):
            gop = n * idx
            if gop > N:
                continue

            if switch[gop] == 1:
                switch[gop] = 0
            else:
                switch[gop] = 1

    # 여학생일 경우
    else:
        if switch[n] == 1:
            switch[n] = 0
        else:
            switch[n] = 1

        for idx in range(1, N + 1):
            p, m = n + idx, n - idx
            if 1 <= p <= N and 1 <= m <= N:
                if switch[p] == switch[m] and switch[p] == 1:
                    switch[p], switch[m] = 0, 0
                elif switch[p] == switch[m] and switch[p] == 0:
                    switch[p], switch[m] = 1, 1
                elif switch[p] != switch[m]:
                    break


N = int(input())        # 스위치 개수

switch = [0] + list(map(int, input().split()))  # 스위치 상태

nos = int(input())          # 학생 수

for _ in range(nos):
    S, Num = map(int, input().split())
    convert(S, Num)

for idx in range(1, N + 1):
    print(switch[idx], end=' ')
    if idx % 20 == 0:
        print()
