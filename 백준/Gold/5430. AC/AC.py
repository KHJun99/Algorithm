from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    if n == 0:
        dq = deque()

    else:
        arr = arr[1 : -1]
        if arr:
            dq = deque(map(int, arr.split(',')))
        else:
            dq = deque()

    is_reversed = False
    error = False

    for alpha in p:
        if alpha == 'R':
            is_reversed = not is_reversed
        elif alpha == 'D':
            if not dq:
                error = True
                break

            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print('error')
    else:
        if is_reversed:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')