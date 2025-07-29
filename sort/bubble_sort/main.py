
def bubble_sort_v1(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

