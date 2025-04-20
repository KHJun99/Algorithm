import sys

n = int(sys.stdin.readline())
member = {}

for i in range(n):
    name, state = sys.stdin.readline().split()
    member[name] = state

for key in list(member.keys()):
    if member[key] == 'leave':
        del member[key]

for name in sorted(member.keys(), reverse=True):
    print(name)