N = int(input())

Score_1 = [ int(x) for x in input().split() ]
Score_2 = []
Sum = 0

for i in range(N):
    Score_2.append(Score_1[i] / max(Score_1) * 100)

for i in range(N):
    Sum += Score_2[i]

mean = Sum / N
print(mean)