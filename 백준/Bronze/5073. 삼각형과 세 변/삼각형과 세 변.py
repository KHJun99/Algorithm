line = []

while True:
    sides = list(map(int, input().split()))

    if sides == [0, 0, 0]:
        break

    line.append(sides)

    # 최대 변과 나머지 두 변의 합 비교
    if max(sides) >= sum(sides) - max(sides):
        print('Invalid')
    else:
        if sides[0] == sides[1] == sides[2]:
            print('Equilateral')
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            print('Isosceles')
        else:
            print('Scalene')
