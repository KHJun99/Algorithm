def Cacu (a, b, c):
    if a >= 1 and c <= 10  ** 12:
        total = a + b + c

        print(total)

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

Cacu(a, b, c)