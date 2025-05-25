# 큐와 스택의 이해를 시험하는 문제
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 자료구조 종류 A 입력 (0 : 큐, 1 : 스택)
A = list(map(int, input().split()))

# 각 자료구조에 들어있는 초기 값 B 입력
B = list(map(int, input().split()))

# 삽입할 수열 C의 길이 M 입력
m = int(input())

# 삽입할 수열 C 입력
C = list(map(int, input().split()))

# 핵심 로직 : 스택인 곳은 무시하고 큐인 곳의 초기 값만 저장
# 큐는 FIFO(선입선출)이므로, 나중에 들어온 값일수록 먼저 나옴
# 그래서 뒤에서부터 큐인 자료구조의 값을 저장하면 나중에 출력할 때 편함
result = deque()
for i in range(n - 1, -1, -1):  # 뒤에서부터 순회
    if A[i] == 0:               # 큐(Queue)인 경우
        result.append(B[i])     # 초기 값을 결과 덱에 추가

# 새로운 값들을 삽입
# 큐인 자료구조를 통과하는 값들이 결국 결과에 추가됨
# 저장된 초기 값들 뒤에 삽입할 수열 C의 값들을 붙이면 됨
for val in C:
    result.append(val)

# 문제에서 요구하는 만큼만 출력 (m개)
# 결과 덱의 앞에서부터 m개를 출력
print(*list(result)[:m])