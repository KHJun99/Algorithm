A1, B1 = map(int,input().split())

A2, B2 = list(map(int,str(A1))), list(map(int,str(B1)))

A3, B3 = [], []

for i in reversed(A2):
    A3.append(i)
for i in reversed(B2):
    B3.append(i)

if A3 > B3:
    for i in A3:
        print(i, end = "")
else:
    for i in B3:
        print(i, end = "")
