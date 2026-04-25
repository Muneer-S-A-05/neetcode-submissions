# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        # if one of the nodes is root
        if p.val==res.val or q.val==res.val:
            return root
        p1,q1=root,root
        while True:
            # finding the nodes
            if p.val==p1.val:
                pass
            else:
                p1 = p1.right if p.val>p1.val else p1.left
            if q.val==q1.val:
                pass
            else:
                q1 = q1.right if q.val>q1.val else q1.left
            # checking if they are still at common nodes
            # if they split path at any point, that is the common node
            # works because we know nodes exist for sure
            if p1.val!=q1.val:
                return res
            else:
                res = p1