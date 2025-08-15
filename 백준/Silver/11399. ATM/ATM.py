# ATM

N = int(input())
pi = list(map(int, input().split()))

sort_pi = sorted(pi)

total = []
time = 0
for i in range(N):
    total.append(sort_pi[i])
    time += sum(total)

print(time)