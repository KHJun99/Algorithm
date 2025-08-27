N = int(input())

bag = 0
while True:
    if N % 5 == 0:
        bag += N // 5
        break
    else:
        N -= 3
        bag += 1
        if N < 0:
            bag = -1
            break

print(bag)