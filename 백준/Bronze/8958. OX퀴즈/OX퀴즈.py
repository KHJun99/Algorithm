T = int(input())

for tc in range(T):
    ox = input().strip()

    total = 0
    score = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)