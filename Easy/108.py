from ast import List
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        len_nums = len(nums)

        if len_nums == 0:
            return None
        
        if len_nums == 1:
            return TreeNode(nums[0])

        root = self.helper(left_index=0, right_index=len_nums-1, nums=nums)
        return root 

    def helper(self, left_index, right_index, nums):
        
        if left_index > right_index:
            return None

        middle_index = (left_index + right_index) // 2

        root = TreeNode(nums[middle_index])
        root.left = self.helper(left_index=left_index, right_index=middle_index - 1, nums=nums)
        root.right = self.helper(left_index=middle_index + 1, right_index=right_index, nums=nums)

        return root