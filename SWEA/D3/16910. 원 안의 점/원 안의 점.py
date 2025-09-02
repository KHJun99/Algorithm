T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[None] * (N + 1) for _ in range(N + 1)]
    point = 0
    for r in range(-N, N + 1):
        for c in range(-N, N + 1):
            visited[r][c] = True
            if (r*r + c*c) <= N*N and visited:
                point += 1

    print(f'#{tc} {point}')
