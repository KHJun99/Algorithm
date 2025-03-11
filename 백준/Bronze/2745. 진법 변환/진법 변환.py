N, B = input().split()
N = list(N)
B = int(B)
result = 0

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(N)):
    if N[i] in alphabet:
        N[i] = alphabet.index(N[i]) + 10
    else:
        N[i] = int(N[i])  # 숫자일 경우 정수로 변환

for j in range(len(N)):
    result += N[len(N) - 1 - j] * (B ** j)  # B의 j 제곱으로 수정

print(result)
