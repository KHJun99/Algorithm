import sys

input = sys.stdin.readline

n, m = map(int, input().split())
people1 = set()
people2 = set()

for i in range(n):
    people1.add(input().strip())

for i in range(m):
    people2.add(input().strip())

result = sorted(people1 & people2)

print(len(result))
for name in result:
    print(name)