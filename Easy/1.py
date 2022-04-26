from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        len_num = len(nums)
        for i in range(len_num):
            for j in range(i, len_num):
                value = nums[i] + nums[j]

                if value == target:
                    return [i, j]

    
solution_object = Solution()

nums_input = [3, 2, 4]
target_input = 6
result = solution_object.twoSum(nums=nums_input, target=target_input)
print(result)