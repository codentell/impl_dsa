def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False