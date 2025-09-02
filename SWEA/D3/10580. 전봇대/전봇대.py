T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pipe = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        pipe.append((ai, bi))

    cross = 0
    for i in range(N):
        for j in range(i + 1, N):
            if pipe[i][0] < pipe[j][0] and pipe[i][1] > pipe[j][1]:
                cross += 1
            if pipe[i][0] > pipe[j][0] and pipe[i][1] < pipe[j][1]:
                cross += 1
    print(f'#{tc} {cross}')