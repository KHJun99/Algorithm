def solution(n, tops):
    MOD = 10007
    dp0, dp1 = 1, 0  # 초기값: 아무 열도 처리 안 한 상태

    for i in range(n):
        mul = 2 if tops[i] == 1 else 1  # tops=1이면 세로마름모 추가

        new_dp0 = (dp0 * (mul + 1) + dp1 * mul) % MOD
        new_dp1 = (dp0 + dp1) % MOD

        dp0, dp1 = new_dp0, new_dp1

    return (dp0 + dp1) % MOD