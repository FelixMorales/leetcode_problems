from typing import List
import numpy as np

def maxSubArray(nums: List[int]):

    maxEndingHere = nums[0]
    maxSoFar = nums[0]

    for num in nums[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


r = maxSubArray([-1,-4,-5,-7,100, 2])
print(r)