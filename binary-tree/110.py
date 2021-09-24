from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0, True
        
        ldepth, lflag = self.maxDepth(root.left)
        rdepth, rflag = self.maxDepth(root.right)
        depth = max(ldepth, rdepth) + 1

        if not lflag or not rflag:
            return depth, False
        
        if abs(ldepth - rdepth) > 1:
            return depth, False
        
        return depth, True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, flag =  self.maxDepth(root)
        return flag