from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        # left_arr = self.postorderTraversal(root.left)
        # right_arr = self.postorderTraversal(root.right)
        # left_arr.extend(right_arr)
        # left_arr.append(root.val)
        # return left_arr
        
        ans = []
        stack = collections.deque()
        # The first recursion to the most left leaf.
        left = root
        while left is not None:
            stack.append(left)
            left = left.left

        pre = None
        cur = None
        while len(stack) > 0:
            cur = stack[-1]
            # When iterate over cur's left subtree, we
            # iterate to cur's right most left leaf.
            if pre is None or pre.left == cur or pre.right == cur:
                if cur.left is not None:
                    stack.append(cur.left)
                elif cur.right is not None:
                    stack.append(cur.right)
                else:
                    ans.append(cur.val)
                    stack.pop()
            elif pre == cur.left:
                if cur.right is not None:
                    stack.append(cur.right)
                else:
                    ans.append(cur.val)
                    stack.pop()
            elif pre == cur.right:
                ans.append(cur.val)
                stack.pop()
            pre = cur
            
        return ans