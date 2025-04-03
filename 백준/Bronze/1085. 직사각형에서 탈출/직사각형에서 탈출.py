x, y, w, h = map(int, input().split())
array = [0, 0, w, h]

dist1 = abs(array[0] - x)
dist2 = abs(array[1] - y)
dist3 = abs(array[2] - x)
dist4 = abs(array[3] - y)

print(min(dist1, dist2, dist3, dist4))
