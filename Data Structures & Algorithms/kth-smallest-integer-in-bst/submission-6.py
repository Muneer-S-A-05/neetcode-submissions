# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c=[0]
        def inorder(node):
            if not node:
                return
            if inorder(node.left):
                return 1
            c[0]+=1
            if c[0]==k:
                c.append(node.val)
                return 1
            if inorder(node.right):
                return 1
        inorder(root)
        return c[1]