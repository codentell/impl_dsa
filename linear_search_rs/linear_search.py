import timeit
import random
import linear_search_rs 
import numpy as np

def linear_search_py(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return True
    return False

nums = np.array(range(100_000_000), dtype=np.int32)  # 10 million integers
target = 999_999_999              # worst-case position

print("Rust (via Maturin):")
print(timeit.timeit(lambda: linear_search_rs.linear_search(nums, target), number=1000))

print("Python:")
print(timeit.timeit(lambda: linear_search_py(nums, target), number=1000))  

