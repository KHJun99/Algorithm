
# 테스트 케이스 개수 설정 / 하드 코딩일 때는 숫자로 설정
T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 방의 가로 길이
    box_list = list(map(int, input().split()))

    drop = 0
    for i in range(N):
        count = 0
        for j in range(i + 1, N):
            if box_list[i] > box_list[j]:
                count += 1
        if drop < count:
            drop = count
    print(f'#{tc} {drop}')
