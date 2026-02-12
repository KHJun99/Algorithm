T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = N % H if N % H != 0 else H
    room = (N - 1) // H + 1
    
    print(f'{floor}{room:02d}')