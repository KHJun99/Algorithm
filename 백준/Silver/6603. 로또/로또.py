def subset(cnt, start):
    if cnt == 6:
        print(*q)
        return

    for i in range(start, k):
        q.append(lst[i])
        subset(cnt+1, i+1)
        q.pop()

while True:
    lst = list(map(int, input().split()))
    k = lst.pop(0)
    if k == 0:
        break

    q = []
    subset(0, 0)
    print()