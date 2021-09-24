from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkSymmetric(self, root0, root1):
        if root0 is None and root1 is None:
            return True
        
        if root0 is None or root1 is None:
            return False
        
        if root0.val != root1.val:
            return False
        
        left = self.checkSymmetric(root0.left, root1.right)
        right = self.checkSymmetric(root0.right, root1.left)
        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.checkSymmetric(root.left, root.right)