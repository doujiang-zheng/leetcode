from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        if root is not None:
            que.append(root)

        have_child = True
        while len(que) > 0:
            top = que.popleft()
            if top.left is None:
                have_child = False
            else:
                if not have_child:
                    return False
                que.append(top.left)

            if top.right is None:
                have_child = False
            else:
                if not have_child:
                    return False
                que.append(top.right)

        return True