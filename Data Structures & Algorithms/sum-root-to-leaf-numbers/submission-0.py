# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:

        def dfs(node,v,res):

            if not node:
                return 0

            v = v*10+node.val

            if not node.left and not node.right:
                res += v
                return res
            res += dfs(node.left,v,res) + dfs(node.right,v,res)

            return res

        return dfs(root,0,0)