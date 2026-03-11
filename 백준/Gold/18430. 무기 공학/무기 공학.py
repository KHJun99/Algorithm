def calc(a, b, c):
    return (2 * a) + b + c

def boomerang(cx, cy):
    global result_max

    if cx == N:
        result_max = max(result_max, sum(score))
        return

    if visited[cx][cy]:
        if cy + 1 < M:
            boomerang(cx, cy + 1)
        else:
            boomerang(cx + 1, 0)
        return

    delta = [(0, -1, 1, 0), (-1, 0, 0, -1), (-1, 0, 0, 1), (0, 1, 1, 0)] 

    for dx1, dy1, dx2, dy2 in delta:
        nx1, ny1 = cx + dx1, cy + dy1
        nx2, ny2 = cx + dx2, cy + dy2
        
        if not (0 <= nx1 < N and 0 <= ny1 < M): continue
        if not (0 <= nx2 < N and 0 <= ny2 < M): continue

        if not visited[nx1][ny1] and not visited[nx2][ny2]:
            score.append(calc(intensity[cx][cy], intensity[nx1][ny1], intensity[nx2][ny2]))
            visited[cx][cy] = True
            visited[nx1][ny1] = True
            visited[nx2][ny2] = True

            if cy + 1 < M:
                boomerang(cx, cy + 1)
            else:
                boomerang(cx + 1, 0)

            # 백트래킹
            score.pop()
            visited[cx][cy] = False
            visited[nx1][ny1] = False
            visited[nx2][ny2] = False
    
    if cy + 1 < M:
        boomerang(cx, cy + 1)
    else:
        boomerang(cx + 1, 0)


N, M = map(int, input().split())
intensity= [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
score = []
result_max = 0

boomerang(0, 0)
print(result_max)