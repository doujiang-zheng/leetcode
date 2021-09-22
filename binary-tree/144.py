from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        
        # left_arr = self.preorderTraversal(root.left)
        # right_arr = self.preorderTraversal(root.right)

        # left_arr.insert(0, root.val)
        # left_arr.extend(right_arr)
        # return left_arr
        ans = []
        stack = deque()
        stack.append(root)
        while stack:
            top = stack.pop()
            if top is not None:
                ans.append(top)
                stack.append(top.right)
                stack.append(top.left)
        return ans



