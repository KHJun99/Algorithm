import sys

n, m = map(int, sys.stdin.readline().split())

pocketmon_dict = {}

for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    pocketmon_dict[i] = a
    pocketmon_dict[a] = i

for _ in range(m):
    quest = sys.stdin.readline().rstrip()
    if quest.isdigit():
        print(pocketmon_dict[int(quest)])
    else:
        print(pocketmon_dict[quest])
