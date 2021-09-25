from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        levs = []
        que = deque()
        if root is not None:
            que.append((root, 1))
        
        while len(que) > 0:
            top, lev = que.popleft()
            if len(levs) == 0 or lev > levs[-1]:
                ans.append([])
                ans[-1].append(top.val)
                levs.append(lev)
            else:
                ans[-1].append(top.val)

            if top.left is not None:
                que.append((top.left, lev + 1))
            if top.right is not None:
                que.append((top.right, lev + 1))
        return ans