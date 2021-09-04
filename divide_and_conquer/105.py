from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0:
            return None

        val = preorder[0]
        idx = -1
        for i in range(len(inorder)):
            if inorder[i] == val:
                idx = i
                break
        root = TreeNode(val)

        left_preorder = preorder[1:idx+1]
        left_inorder = inorder[:idx]
        left = self.buildTree(left_preorder, left_inorder)
        root.left = left

        right_preorder = preorder[idx+1:]
        right_inorder = inorder[idx+1:]
        right = self.buildTree(right_preorder, right_inorder)
        root.right = right
        return root

if __name__ == '__main__':
    sol = Solution()
    preorders = [[3, 9, 20, 15, 7], [-1]]
    inorders = [[9, 3, 15, 20, 7], [-1]]
    for preorder, inorder in zip(preorders, inorders):
        # root = sol.buildTree(preorder, inorder)
        print(sol.buildTree(preorder, inorder))
