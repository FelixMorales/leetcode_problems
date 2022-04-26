# Definition for a binary tree node.
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left: TreeNode = left
         self.right: TreeNode = right
class Solution:
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def isSameTree(self, p, q):

            if not p and not q:
                return True
      
            if not q or not p:
                return False

            if p.val != q.val:
                return False
                
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
                

        