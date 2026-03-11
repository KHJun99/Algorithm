H, W = map(int, input().split())
heights = list(map(int, input().split()))

left, right = [], []

for idx in range(W):
    left_lst = heights[:idx]
    right_lst = heights[idx:]

    left.append(max(left_lst) if left_lst else 0)
    right.append(max(right_lst) if right_lst else 0)

result = 0
for idx in range(W):
    amount = min(left[idx], right[idx]) - heights[idx]
    
    if amount >= 0:
        result += amount

print(result)