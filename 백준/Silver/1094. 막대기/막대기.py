def binary_to_decimal(n):
    decimal_num = ''
    pow = 0

    while n > 0:
        if n % 2 == 1:
            decimal_num = '1' + decimal_num
        else:
            decimal_num = '0' + decimal_num
        n //= 2

    return decimal_num


X = int(input())
dec_X = binary_to_decimal(X)

cnt = 0

for i in range(len(dec_X)):
    if dec_X[i] == '1':
        cnt += 1

print(cnt)