N = int(input())

max_len = 0
best = []
for i in range(1, N + 1):
    num1, num2 = N, i
    lst = [num1, num2]

    while True:
        nxt = num1 - num2
        if nxt < 0:
            break
        lst.append(nxt)
        num1, num2 = num2, nxt

    if len(lst) > max_len:
        max_len = len(lst)
        best = lst

print(len(best))
print(*best)