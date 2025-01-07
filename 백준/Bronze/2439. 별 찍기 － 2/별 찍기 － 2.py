N = int(input())
r = N

for i in range(1, N+1, 1):
    print(str('*' * i).rjust(r))