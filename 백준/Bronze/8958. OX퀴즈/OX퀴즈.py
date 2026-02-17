T = int(input())

result = []
for _ in range(T):
    OX = input()

    score = 0
    point = 0
    for ox in OX:
        if ox == 'O':
            score += 1
            point += score
        else:
            score = 0
    
    result.append(point)

for row in result:
    print(row)