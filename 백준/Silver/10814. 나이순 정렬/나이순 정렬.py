import sys
n = int(sys.stdin.readline())
member = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member.append([age, name])

member_sorted = sorted(member, key = lambda x: x[0])

for age, name in member_sorted:
    print(age, name)