N = int(input())

Num = int(input())
Num_list = list(map(int, str(Num)))

sum = 0

for i in range(min(N, len(Num_list))):
    sum += Num_list[i]

print(sum)

