H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
elif M < 45 and H > 0 and H < 24:
    print(H - 1, 60 - (abs(M - 45)))
elif M < 45 and H == 0:
    print('23', 60 - (abs(M - 45)))
