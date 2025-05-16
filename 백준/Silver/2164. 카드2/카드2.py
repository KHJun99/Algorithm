# 큐를 사용하여 동작을 구현하는 문제
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

card = deque()

for i in range(1, n + 1):
    card.append(i)

for _ in range(n):
    if len(card) > 1:
        card.popleft()
        next_card = card.popleft()
        card.append(next_card)
    elif len(card) == 1:
        break

print(*card)