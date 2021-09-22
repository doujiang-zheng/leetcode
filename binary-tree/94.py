from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        
        # left_arr = self.inorderTraversal(root.left)
        # right_arr = self.inorderTraversal(root.right)
        # left_arr.append(root.val)
        # left_arr.extend(right_arr)
        # return left_arr
        stack = collections.deque()
        ans = []

        if root is not None:
            ch = root
            while ch is not None:
                stack.append(ch)
                ch = ch.left
        
        while stack:
            top = stack.pop()
            ans.append(top.val)
            ch = top.right
            while ch is not None:
                stack.append(ch)
                ch = ch.left
        
        return ans