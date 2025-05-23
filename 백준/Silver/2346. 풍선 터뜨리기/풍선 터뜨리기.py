# 덱을 활용하여 배열을 양방향으로 돌리는 문제
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
balloons = deque(enumerate(map(int, input().split()), 1))  # 풍선 번호랑 같이 저장!
result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(str(idx))

    if move > 0:
        balloons.rotate(-(move - 1))  # 양수면 오른쪽으로 (시계 방향)
    else:
        balloons.rotate(-move)  # 음수면 왼쪽으로 (반시계 방향)

print(' '.join(result))