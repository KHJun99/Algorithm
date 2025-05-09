import math

# 입력 받기
n = int(input())

# 제곱수의 개수는 sqrt(n)을 내림한 값과 같음
# 예를 들어 n=10이면 sqrt(10)은 약 3.16 -> 내림하면 3 (제곱수는 1, 4, 9)
# n=25이면 sqrt(25)는 5 -> 내림하면 5 (제곱수는 1, 4, 9, 16, 25)
result = int(math.sqrt(n))

# 결과 출력
print(result)