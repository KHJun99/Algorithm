import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
num = list()

for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    lcm = a * b // g
    num.append(lcm)

for i in num:
    print(i)

