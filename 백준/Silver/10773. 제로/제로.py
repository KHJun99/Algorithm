import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

money = []
for _ in range(n):
    command = int(input())

    if command != 0:
        money.append(command)
    else:
        money.pop()

print(str(sum(money)))
