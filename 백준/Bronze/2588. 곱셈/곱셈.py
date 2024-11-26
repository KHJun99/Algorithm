def Cacu (a, b):
    b1 = b % 10
    b2 = (b - ((b // 100) * 100)) // 10
    b3 = b // 100

    A = a * b1
    B = a * b2
    C = a * b3
    D = a * b

    print(A)
    print(B)
    print(C)
    print(D)

a = int(input())
b = int(input())

Cacu(a, b)