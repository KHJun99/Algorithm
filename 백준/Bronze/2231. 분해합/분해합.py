N = int(input())
length = len(str(N))

start = max(0, N - (9 * length))
for num in range(start, N):
    if num + sum(map(int, str(num))) == N:
        print(num)
        break
else:
    print(0)