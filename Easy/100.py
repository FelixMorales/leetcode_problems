# Definition for a binary tree node.
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:
        def isSameTree(self, p: TreeNode, q: TreeNode):

            if not p and not q:
                return True
      
            if not q or not p:
                return False

            if p.val != q.val:
                return False
                
            same_left_tree = self.isSameTree(p.left, q.left)
            same_right_tree = self.isSameTree(p.right, q.right)

            result = same_right_tree and same_left_tree
            return result
                

        