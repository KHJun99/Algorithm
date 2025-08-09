T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        lower_right = 0
        for j in range(i + 1, N):
            if box[i] > box[j]:
                lower_right += 1
        if lower_right > ans:
            ans = lower_right

    print(f'#{tc} {ans}')