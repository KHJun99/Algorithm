import sys

n = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))
result = []

_dict = {}
for i in range(len(card1)):
    _dict[card1[i]] = 0
    
for j in range(m):
    if card2[j] not in _dict:
        print(0, end = ' ')
    else:
        print(1, end = ' ')