T = int(input())
C = []
change = [25, 10, 5, 1]

for i in range(T):
    C.append(int(input()))

for i in range(len(C)):
    for j in range(len(change)):
        a = C[i] // change[j]
        C[i] -= a * change[j]
        print(int(a), end = " ")
    print()