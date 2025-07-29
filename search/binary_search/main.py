def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target: 
            return True 
        elif nums[mid] > target:
            if mid == 0: 
                break
            right = mid - 1
        else: 
            left = mid + 1

    