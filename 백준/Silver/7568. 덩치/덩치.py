N = int(input())
physical = []

for _ in range(N):
    weight, height = map(int, input().split())
    physical.append([weight, height])

rank = []
count = 1

for i in range(N):
    for j in range(N - 1):
        if physical[0][0] < physical[j + 1][0] and physical[0][1] < physical[j + 1][1]:
            count += 1
    rank.append(count)
    count = 1
    physical.append(physical.pop(0))

print(*rank)