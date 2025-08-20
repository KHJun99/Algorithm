for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    while password[-1] != 0:
        for i in range(1, 6):
            tmp = password[0]
            if tmp - i > 0:
                password.append(tmp - i)
                password.pop(0)
            else:
                password.append(0)
                password.pop(0)
                break

    print(f'#{tc}', *password)