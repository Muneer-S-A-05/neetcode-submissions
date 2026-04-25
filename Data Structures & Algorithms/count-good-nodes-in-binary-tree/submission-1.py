# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # creating new function as we need to know max value in path from root yet
        def dfs(node,maxVal):
            if not node: return 0
            # 1 if no greater guy in path yet
            # that means good buoy
            res = 1 if node.val >= maxVal else 0
            # updating max in case got bigger buoy
            maxVal = max(maxVal,node.val)
            return dfs(node.left,maxVal) + dfs(node.right,maxVal) + res
        return dfs(root,root.val)