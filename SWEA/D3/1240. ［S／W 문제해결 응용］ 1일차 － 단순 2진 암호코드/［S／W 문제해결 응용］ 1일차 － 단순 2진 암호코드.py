def binary_password(lst,n,m):
    password = []
    for i in range(n):
        j = m
        while j >= 0:
            windows = ''.join(lst[i][j:j - 7:-1])
            if len(password) == 8:
                return password
            if windows in pw:
                password.append(pw[windows])
                j -= 7
            else:
                j -= 1
    return password


pw = {
    '1011000' : 0,
    '1001100' : 1,
    '1100100' : 2,
    '1011110' : 3,
    '1100010' : 4,
    '1000110' : 5,
    '1111010' : 6,
    '1101110' : 7,
    '1110110' : 8,
    '1101000' : 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N : 배열의 세로 크기, M : 배열의 가로 크기
    arr = [list(input()) for _ in range(N)]

    password = binary_password(arr, N, M)
    password.reverse()
    pw_sum = 0

    if ((sum(password[0:8:2]) * 3) + sum(password[1:8:2])) % 10 == 0:
        for i in password:
            pw_sum += i
    else:
        pw_sum = 0

    print(f'#{tc} {pw_sum}')