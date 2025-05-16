# 큐의 개념을 익히고 실습하는 문제 - deque 사용 버전 (시간 단축!)
from collections import deque # deque 불러오기
import sys

input = sys.stdin.readline

n = int(input())

# queue = [] # 리스트 대신
queue = deque() # deque로 큐 초기화! 이게 핵심!

for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'push':
        queue.append(command[1]) # push는 deque도 append (맨 뒤에 추가)
    elif command[0] == 'pop':
        if queue:
            # item = queue.pop(0) # 리스트의 pop(0) 대신
            item = queue.popleft() # deque는 맨 앞에서 뺄 때 popleft() 사용!
            print(item)
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(queue)) # deque도 len은 O(1)
    elif command[0] == 'empty':
        if not queue: # deque가 비어있으면 True
            print('1')
        else:
            print('0')
    elif command[0] == 'front':
        if queue:
            print(queue[0]) # deque도 인덱스로 맨 앞 요소 접근 가능 (O(1))
        else:
            print('-1')
    elif command[0] == 'back':
        if queue:
            print(queue[-1]) # deque도 인덱스로 맨 뒤 요소 접근 가능 (O(1))
        else:
            print('-1')
