def one_two_three(n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return(dp[n])


# n은 양수이며 11보다 작기 때문
dp = [0] * 11
T = int(input())
for tc in range(T):
    n = int(input())

    cnt = one_two_three(n)
    print(cnt)