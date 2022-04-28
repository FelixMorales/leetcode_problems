from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:

        def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

            if not root:
                return False
            
            r = self.helper(node=root, current_sum=root.val, target=targetSum)

            return r
        
        def helper(self, node: TreeNode, current_sum: int, target: int):
            if not node.left and not node.right:
                if target == current_sum:
                    return True
            else:
                r = False
                if node.left:
                    r = self.helper(node=node.left, current_sum=current_sum+node.left.val, target=target)
                
                if node.right and not r:
                    self.helper(node=node.right, current_sum=current_sum+node.right.val, target=target)
                
                return r