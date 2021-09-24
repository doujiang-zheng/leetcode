from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val > key:
            left = self.deleteNode(root.left, key)
            root.left = left
        elif root.val == key:
            if root.left is not None:
                # move root.right to the left subtree
                tmp = root.right
                pre = root.left
                while pre.right is not None:
                    pre = pre.right
                pre.right = tmp
                # replace root with the left subtree
                root = root.left
            elif root.right is not None:
                # root.left == None and root.right != None
                root = root.right
            else:
                # root.left == None and root.right == None
                root = None 
        else:
            right = self.deleteNode(root.right, key)
            root.right = right

        return root