H, W, N, M = map(int, input().split())

row = (H - 1) // (N + 1) + 1
col = (W - 1) // (M + 1) + 1

print(row * col)