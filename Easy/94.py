from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        array = []
        
        self.inOrder(node=root, result=array)

        return array

    def inOrder(self, node: TreeNode, result: List[int]):

        if node.left:
            self.inOrder(node=node.left, result=result)
        
        result.append(node.val)

        if node.right:
            self.inOrder(node=node.right, result=result)


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)


sol = Solution()

r = sol.inorderTraversal(root=tree)
print(r)


