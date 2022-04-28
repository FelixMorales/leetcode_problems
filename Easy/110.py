from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:
        
        def __init__(self) -> None:
            self.depths = []

        def isBalanced(self, root: Optional[TreeNode]) -> bool:

            if not root:
                return True
            
            if not root.left and not root.right:
                return True
            
            r = self.helper(node=root)

            return r

        def helper(self, node: TreeNode):
            
            depth_left = 0
            depth_right = 0

            if not node:
                return True

            if node.left:
                depth_left = self.get_depth(node=node.left, current_depth=1)
            
            if node.right:
                depth_right = self.get_depth(node=node.right, current_depth=1)
            
            if depth_left > depth_right + 1:
                return False
            
            if depth_left < depth_right - 1:
                return False
            
            return self.helper(node=node.left) and self.helper(node=node.right)
            
        
        def get_depth(self, node: TreeNode, current_depth: int):
            if not node.left and not node.right:
                return current_depth
            else:
                left_depth = 0
                right_depth = 0
                
                if node.left:
                    left_depth = self.get_depth(node=node.left, current_depth=current_depth+1)
                
                if node.right:
                    right_depth = self.get_depth(node=node.right, current_depth=current_depth+1)
                
                return max(left_depth, right_depth)
            
tree = TreeNode(1)

tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.left.left.left = TreeNode(7)

tree.right.right = TreeNode(6)

tree.right.right.right = TreeNode(8)

sol = Solution()

print(sol.isBalanced(tree))