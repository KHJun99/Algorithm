import sys
import math

input = sys.stdin.readline

def isprime(num):
    # 주어진 수가 소수인지 판별하는 함수. 소수면 True, 아니면 False 반환
    if num < 2:              # 2보다 작은 수는 소수가 아님
        return False
    if num == 2:             # 2는 유일한 짝수 소수
        return True
    if num % 2 == 0:         # 2를 제외한 짝수는 모두 소수가 아님
        return False
    # 3부터 √num까지 홀수만 검사
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:     # 나눠지는 수가 있으면 소수가 아님
            return False
    return True              # 위 조건을 모두 통과하면 소수

n, m = map(int, input().strip().split())
result = []

for i in range(n, m + 1):
    if isprime(i):
        result.append(i)

for i in result:
    print(i)