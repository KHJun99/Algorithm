def solution(nums):
    pick = len(nums) // 2
    type = len(set(nums))
    
    return min(pick, type) 