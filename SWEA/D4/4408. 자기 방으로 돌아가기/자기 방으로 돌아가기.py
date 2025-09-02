T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 돌아가야 할 학생들의 수
    corridor = [0] * 201
    for room in range(N):
        cur, nxt = map(int, input().split())
        if cur > nxt:
            cur, nxt = nxt, cur

        cur = (cur + 1) // 2
        nxt = (nxt + 1) // 2

        for i in range(cur, nxt + 1):
            corridor[i] += 1
    result = max(corridor)
    print(f'#{tc} {result}')