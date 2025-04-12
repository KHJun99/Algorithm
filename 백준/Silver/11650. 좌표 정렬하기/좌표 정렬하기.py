import sys
input = sys.stdin.readline

coordinate = []

n = int(input())

for i in range(n):
    [a, b] = map(int, input().split())
    coordinate.append([a, b])

coordinate.sort()

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])