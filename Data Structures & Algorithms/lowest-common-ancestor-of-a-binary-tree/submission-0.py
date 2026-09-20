# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        def dfs(node):
            if not node: return False
            left = dfs(node.left)
            right = dfs(node.right)

            if (node.val in (p.val,q.val) and (left or right)) or (left and right):
                res[0] = node
            return node.val in (p.val,q.val) or left or right
        
        dfs(root)
        return res[0]