import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result1 = len(a - b)
result2 = len(b - a)
print(result1 + result2)
