class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:
        
        def __init__(self) -> None:
            self.min_depth = None

        def minDepth(self, root: TreeNode):

            if not root:
                return 0
            
            self.helper(node=root, current_depth=1)

            return self.min_depth
        
        def helper(self, node: TreeNode, current_depth: int):
            if not node.left and not node.right:
                if self.min_depth:
                    self.min_depth = min(self.min_depth, current_depth)
                else:
                    self.min_depth = current_depth
            
            else:
                if node.left:
                    self.helper(node=node.left, current_depth=current_depth+1)
                
                if node.right:
                    self.helper(node=node.right, current_depth=current_depth+1)
    