def linear_search1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

def linear_search2(nums, target):
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] == target:
            return True
        start += 1 
    return False 



