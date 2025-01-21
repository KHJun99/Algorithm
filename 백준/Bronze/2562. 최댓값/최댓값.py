Array = []

for i in range(9):
    Array.append(int(input()))

max_index = Array.index(max(Array)) + 1

print(max(Array))
print(max_index)