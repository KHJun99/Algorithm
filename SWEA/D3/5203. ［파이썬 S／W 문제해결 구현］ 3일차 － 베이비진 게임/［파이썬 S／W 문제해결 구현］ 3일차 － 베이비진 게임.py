def is_babygin(cnt):
    # triple : 같은 숫자 3장
    for k in range(10):
        if cnt[k]  >= 3:
            return True

    # run : 연속된 숫자 3장
    for k in range(8):      # 0~7까지만 확인하면 됨으로
        if cnt[k] and cnt[k + 1] and cnt[k + 2]:        # 세 카드가 1이상이면 True 반환
            return True
    return False


def solve(cards):
    c1 = [0] * 10
    c2 = [0] * 10

    for i, x in enumerate(cards):
        # 짝수 인덱스 : player1 차례
        if i % 2 == 0:
            c1[x] += 1
            if is_babygin(c1):
                return 1

        # 홀수 인덱스 : player2 차례
        else:
            c2[x] += 1
            if is_babygin(c2):
                return 2
    return 0        # 승부가 나지 않을 경우


T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    result = solve(card)
    print(f'#{tc} {result}')