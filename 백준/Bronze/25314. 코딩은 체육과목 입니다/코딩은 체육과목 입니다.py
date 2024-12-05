# 입력 받기
N = int(input())

# N이 4의 배수인지 확인
if N % 4 == 0:
    output = ""
    for _ in range(N // 4):
        output += "long "
    output += "int"
    print(output.strip())
