import sys
input = sys.stdin.readline

coordinate = []
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    coordinate.append((y, x))

coordinate.sort()

for i in range(n):
    print(coordinate[i][1], coordinate[i][0])