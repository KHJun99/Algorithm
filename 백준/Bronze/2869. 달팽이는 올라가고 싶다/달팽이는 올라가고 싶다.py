# 올라가야 할 거리 = length - down
# 하루에 갈 수 있는 거리 = up - down

up, down, length = map(int, input().split())

if (length - down) % (up - down) == 0:              # 낮 동안 정상까지 도착 한 경우
    print((length - down) // (up - down))

else:                                               # 낮 동안 정상까지 도착 못 한 경우
    print((length - down) // (up - down) + 1)