# 이항 계수는 N개의 물건 중 K개를 순서 없이 고르는 경우의 수와 같습니다. 이것도 조합론에서 자주 만나게 될 것입니다.
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def Binomial_Coefficient(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))

print(int(Binomial_Coefficient(n, k)))