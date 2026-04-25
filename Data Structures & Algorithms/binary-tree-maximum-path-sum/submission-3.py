# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float('inf')
        def maxPath(node):
            if not node:
                return 0
            left = maxPath(node.left) + node.val
            right = maxPath(node.right) + node.val
            self.maxSum = max(self.maxSum,left+right-node.val,left,right,node.val)
            return max(left,right,node.val)
        maxPath(root)
        return self.maxSum