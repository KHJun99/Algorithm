nums = []

for _ in range(9):
    num = int(input())
    nums.append(num)

max_num = float('-inf')
max_idx = 0
for idx, num in enumerate(nums, start=1):
    if num > max_num:
        max_num = num
        max_idx = idx
    
print(max_num)
print(max_idx)
