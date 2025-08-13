T = int(input())
for tc in range(1, T + 1):
    N = int(input())     # N : 파스칼 삼각형 크기

    triangle = [[1] * i for i in range(1, N + 1)]

    for i in range(N - 1):
        for j in range(len(triangle[i]) - 1):
            triangle[i + 1][j + 1] = triangle[i][j] + triangle[i][j + 1]

    print(f'#{tc}')
    for i in triangle:
        print(*i)