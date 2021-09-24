from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root):
        if root is None:
            return (None, None, True)
        
        lmin, lmax, lflag = self.check(root.left)
        rmin, rmax, rflag = self.check(root.right)

        if not lflag or not rflag:
            # Propagate False flag.
            return (None, None, False)
        
        flag = True
        if lmax is not None and lmax >= root.val:
            flag = False
        if lmin is None:
            lmin = root.val

        if rmin is not None and rmin <= root.val:
            flag = False
        if rmax is None:
            rmax = root.val
        return lmin, rmax, flag
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, flag = self.check(root)
        return flag