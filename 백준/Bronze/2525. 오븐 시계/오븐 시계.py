# 현재 시간 입력 받기
A, B = map(int, input().split())
# 추가할 시간 입력 받기
C = int(input())

# 현재 시간을 분으로 변환
current_minutes = A * 60 + B

# 추가할 시간을 더하기
total_minutes = current_minutes + C

# 새로운 시간을 계산
new_A = (total_minutes // 60) % 24  # 24시간 형식에 맞게 조정
new_B = total_minutes % 60           # 분 계산

# 결과 출력
print(new_A, new_B)
