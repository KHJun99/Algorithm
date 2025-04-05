n, m = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0

# 카드 리스트를 정렬합니다.
card.sort()

# 3개의 카드 조합을 찾기 위한 중첩 루프
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current_sum = card[i] + card[j] + card[k]
            if current_sum <= m and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)