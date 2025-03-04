Numpy = []
Max = 0
max_position = (0, 0)  # 최대값의 위치를 저장할 변수

# 9x9 행렬 입력
for i in range(9):
    Numpy.append(list(map(int, input().split())))

# 최대값 찾기
for i in range(9):
    for j in range(9):
        if Numpy[i][j] >= Max:
            Max = Numpy[i][j]  # 값을 업데이트
            max_position = (i + 1, j + 1)  # 위치 업데이트 (1-based index)

print(Max)  # 최대값 출력
print(max_position[0], max_position[1])  # 최대값의 위치 출력
