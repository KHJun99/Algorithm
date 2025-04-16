import sys

n, m = map(int, sys.stdin.readline().split())

s_set = set()
for _ in range(n):
    s_set.add(sys.stdin.readline().rstrip())

count = 0
for _ in range(m):
    test = sys.stdin.readline().rstrip()
    if test in s_set:
        count += 1

print(count)
