N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최대 길이 찾기
max_length = max(dp)
print(max_length)

# 역추적으로 실제 수열 찾기
result = []
length = max_length

for i in range(N - 1, -1, -1):
    if dp[i] == length:
        result.append(A[i])
        length -= 1

result.reverse()
print(*result)