import sys

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

num1 = (a * d) + (c * b)
num2 = (b * d)

g = gcd(num1, num2)
result1 = num1 // g
result2 = num2 // g

print(result1, result2)
