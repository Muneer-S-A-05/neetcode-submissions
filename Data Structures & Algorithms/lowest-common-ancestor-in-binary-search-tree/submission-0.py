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
            elif p.val < p1.val:
                p1 = p1.left
            else:
                p1 = p1.right
            if q.val==q1.val:
                pass
            elif q.val < q1.val:
                q1 = q1.left
            else:
                q1 = q1.right
            # checking if they are still at common nodes
            # if they split path at any point, that is the common node
            # works because we know nodes exist for sure
            if p1.val!=q1.val:
                return res
            else:
                res = p1