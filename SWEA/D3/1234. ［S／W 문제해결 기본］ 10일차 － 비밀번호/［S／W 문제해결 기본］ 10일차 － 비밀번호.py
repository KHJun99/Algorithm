T = 10
for tc in range(1, T + 1):
    length, arr = input().split()

    stack = []
    for i in range(int(length)):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    result = ''.join(stack)

    print(f'#{tc} {result}')