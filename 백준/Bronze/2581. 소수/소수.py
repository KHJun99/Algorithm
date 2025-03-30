N = int(input())
M = int(input())

array = []

for i in range(N, M+1):
    is_prime = True
    if i < 2:  # 2 미만의 수는 소수가 아님
        is_prime = False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        array.append(i)

if array:
    print(sum(array))
    print(min(array))

else:
    print('-1')