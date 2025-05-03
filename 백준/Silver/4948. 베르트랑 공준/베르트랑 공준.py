import sys

input = sys.stdin.readline

# 최대 입력값을 저장할 리스트
inputs = []
max_n = 0

# 입력을 모두 받아 저장하고 최대값 계산
while True:
    n = int(input())
    if n == 0:
        break
    inputs.append(n)
    if 2 * n > max_n:
        max_n = 2 * n

# 에라토스테네스의 체: 2부터 max_n까지 소수 판별
sieve = [True] * (max_n + 1)
sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(max_n ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, max_n + 1, i):
            sieve[j] = False  # i의 배수는 소수가 아님

# 각 입력에 대해 n < p ≤ 2n 범위의 소수 개수를 세기
for n in inputs:
    count = sum(sieve[n + 1: 2 * n + 1])
    print(count)
