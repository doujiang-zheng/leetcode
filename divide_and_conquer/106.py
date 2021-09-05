from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) <= 0:
            return None

        val = postorder[-1]
        root = TreeNode(val)

        left_idx = -1
        for i in range(len(inorder)):
            if inorder[i] == val:
                left_idx = i
                break
        left_inorder = inorder[:left_idx]
        left_postorder = postorder[:left_idx]
        left = self.buildTree(left_inorder, left_postorder)
        root.left = left

        right_inorder = inorder[left_idx+1:]
        right_postorder = postorder[left_idx:-1]
        right = self.buildTree(right_inorder, right_postorder)
        root.right = right

        return root


if __name__ == '__main__':
    sol = Solution()
    inorders = [[9, 3, 15, 20, 7], [-1]]
    postorders = [[9, 15, 7, 20, 3], [-1]]
    for inorder, postorder in zip(inorders, postorders):
        print(sol.buildTree(inorder, postorder))
