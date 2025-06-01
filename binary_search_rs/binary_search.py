import timeit
import random
import numpy as np
import binary_search_rs  # This is your compiled PyO3 module via maturin


def binary_search_py(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# --- Test data ---
nums = np.array(range(1_000_000), dtype=np.int32)  # 100 million sorted integers
target = 999_999  # Worst-case position (last index)

print("Rust (via Maturin):")
print(timeit.timeit(lambda: binary_search_rs.binary_search(nums, target), number=1000))

print("Python:")
print(timeit.timeit(lambda: binary_search_py(nums, target), number=1000))

