# 덱의 개념을 익히고 실습하는 문제
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

deck = deque()
for _ in range(n):
    command = list(map(int,input().split()))

    if command[0] == 1:
        deck.appendleft(command[1])

    elif command[0] == 2:
        deck.append(command[1])

    elif command[0] == 3:
        if deck:
            item = deck.popleft()
            print(item)
        else:
            print('-1')

    elif command[0] == 4:
        if deck:
            item = deck.pop()
            print(item)
        else:
            print('-1')

    elif command[0] == 5:
        print(len(deck))

    elif command[0] == 6:
        if not deck:
            print('1')
        else:
            print('0')

    elif command[0] == 7:
        if deck:
            print(deck[0])
        else:
            print('-1')

    elif command[0] == 8:
        if deck:
            print(deck[-1])
        else:
            print('-1')