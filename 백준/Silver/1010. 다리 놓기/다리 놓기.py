# 벌써 만났습니다.
import sys

input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)
