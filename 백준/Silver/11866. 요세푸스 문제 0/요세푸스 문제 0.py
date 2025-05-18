# 큐를 활용하여 배열을 돌리는 문제
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

people = deque(range(1, n + 1)) # 1부터 n까지 바로 deque 생성

out_people = [] # deque 대신 list로 받아도 됨

# 사람이 다 빠져나갈 때까지 반복
while people:
    # k번째 사람을 찾기 위해 k-1번 회전
    # deque의 맨 앞 요소를 k-1번 맨 뒤로 보냄
    people.rotate(-(k-1)) # 왼쪽으로 k-1번 회전 (맨 앞이 k-1번 뒤로)

    # 이제 k번째 사람이 맨 앞에 왔으니 빼냄
    out_people.append(people.popleft())

# 결과 출력
print('<', ', '.join(map(str, out_people)), '>', sep='')