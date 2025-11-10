T = int(input())
for tc in range(1, T + 1):
    B, W, X, Y, Z = map(int, input().split())

    cost1 = B * X + W * Y

    if B > W:
        cost2 = 2 * W * Z + (B - W) * X
    else:
        cost2 = 2 * B * Z + (W - B) * Y

    print(cost1) if cost1 >= cost2 else print(cost2)