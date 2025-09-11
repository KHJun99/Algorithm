# 백준_2798_블랙잭 (B2)
"""
문제
- 플레이어가 고른 카드(3장) 의 합은 M을 넘지 않으면서 M과 최대한 가까운 수를 출력하시오.
"""
import sys

N, M = map(int, input().split())
card = list(map(int, input().split()))

best = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            result = card[i] + card[j] + card[k]
            if result == M:
                print(M)
                sys.exit(0)         # 정확히 맞추면 종료
            if result < M and result > best:
                best = result

print(best)
