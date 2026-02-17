nums = [int(input()) for _ in range(10)]

result = set()
for num in nums:
    result.add(num % 42)

print(len(result))