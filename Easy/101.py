from ast import List
from operator import le
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
         
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:            
        left_subtree = root.left
        right_subtree = root.right

        result = self.helper(left_subtree, right_subtree)

        return result


    def helper(self, l_s: TreeNode, r_s: TreeNode):
        if not l_s and not r_s:
            return True
        
        if not l_s or not r_s:
            return False
        
        if not l_s.right and l_s.left and r_s.left:
            return False
        
        if not l_s.left and l_s.right and r_s.right:
            return False
        
        if l_s.val != r_s.val:
            return False
        
        left_result = self.helper(l_s.left, r_s.right)
        right_result = self.helper(l_s.right, r_s.left)

        return left_result and right_result
        
                

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(sol.isSymmetric(root=root))