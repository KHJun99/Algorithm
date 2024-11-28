H , M = map(int, input().split())
0 <= H <= 23
0 <= M <= 59

TransM = M -45
if TransM < 0:
    TransM = 60 + TransM
    H = H -1
    if H < 0:
        H = 24 + H

print(H,TransM)


