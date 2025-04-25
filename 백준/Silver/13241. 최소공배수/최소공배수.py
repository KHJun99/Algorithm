# 유클리드 호제법 사용

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num = list()

a, b = map(int, input().split())
g = gcd(a, b)
lcm = a * b // g

print(lcm)