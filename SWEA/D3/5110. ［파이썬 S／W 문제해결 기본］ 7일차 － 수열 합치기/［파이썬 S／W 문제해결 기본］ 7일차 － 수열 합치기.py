T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 합쳐질 수열 arr (양의 무한대)
    arr = [float('inf')]
    cnt = 0     # 현재까지 합쳐진 수열 개수
    for _ in range(M):
        a = list(map(int, input().split()))
        for i in range(N * cnt + 1):
            if a[0] < arr[i]:
                arr[i:i] = a        # i 위치에 새 수열 a 전체를 통째로 삽입
                break
        cnt += 1    #합쳐진 수열 개수 증가
    print(f'#{tc}', end=' ')
    print(*arr[-11:-1][::-1])       # arr[-11:-1] 10개 선택