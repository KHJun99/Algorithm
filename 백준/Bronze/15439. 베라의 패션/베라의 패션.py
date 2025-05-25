# 조건을 만족하는 두 옷의 조합을 세는 문제
import sys

input = sys.stdin.readline

n = int(input())

shirt, pants = [], []

for i in range(n):
    shirt.append(i)
    pants.append(i)

count = 0
for i in shirt:
    for j in pants:
        if not i == j:
            count += 1
        else:
            pass

print(count)