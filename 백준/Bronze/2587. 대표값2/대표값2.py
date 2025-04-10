num = []

for i in range(5):
    num.append(int(input()))

# 리스트를 정렬하여 새로운 리스트를 반환
sorted_num = sorted(num)

# 평균 계산
average = int(sum(num) / len(num))

# 중앙값 (정렬된 리스트의 세 번째 요소)
median = sorted_num[2]

print(average)
print(median)
