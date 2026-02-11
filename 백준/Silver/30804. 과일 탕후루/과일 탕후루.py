def make_Tanghulu(n, lst):
    left, right = 0, 0
    max_length = float('-inf')

    fruits_count = {}

    while left != n and right < n:
        fruit = lst[right]
        fruits_count[fruit] = fruits_count.get(fruit, 0) + 1

        if len(fruits_count) <= 2:
            max_length = max(max_length, right - left + 1)
            right += 1
        
        else:
            fruits_count[lst[left]] -= 1
            if fruits_count[lst[left]] == 0:
                del fruits_count[lst[left]]
            left += 1
            right += 1
    
    print(max_length)



N = int(input())

fruits = list(map(int, input().split()))

make_Tanghulu(N, fruits)