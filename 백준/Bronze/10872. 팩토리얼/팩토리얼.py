# 팩토리얼은 N개의 물건을 일렬로 나열하는 경우의 수와 같습니다. 조합론에서 자주 만나게 될 것입니다.
import sys

input = sys.stdin.readline

n = int(input())

result = []
for i in range(1, n + 1):
    if not n == 0:
        result.append(i)
    else:
        result.append('1')

factorial = 1
for i in result:
    factorial = factorial*i

print(factorial)