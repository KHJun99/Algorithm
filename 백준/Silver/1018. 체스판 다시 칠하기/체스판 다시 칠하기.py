n, m = map(int, input().split())

original, count = [], []

for _ in range(n):
    original.append(input())

for a in range(n - 7):                              # 전체 체스판에서 시작점을 잡기 위한 반복문
    for b in range(m - 7):                          # 전체 체스판에서 시작점을 잡기 위한 반복문
        index1 = 0
        index2 = 0
        for i in range(a, a + 8):                   # a는 행, 8 * 8로 자를 수 있는 범위의 시작점
            for j in range(b, b + 8):               # b는 열, 8 * 8로 자를 수 있는 범위의 시작점
                if (i + j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1                 # index1 : 'W'로 시작할 경우 바뀐 체스 판의 개수를 세기 위함
                    if original[i][j] != 'B':       # index2 : 'B'로 시작할 경우 바뀐 체스 판의 개수를 세기 위함
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))