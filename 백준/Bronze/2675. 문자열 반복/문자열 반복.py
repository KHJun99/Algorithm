T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    tmp = ""

    for s in S:
        tmp += (s * R)
    
    print(tmp)
