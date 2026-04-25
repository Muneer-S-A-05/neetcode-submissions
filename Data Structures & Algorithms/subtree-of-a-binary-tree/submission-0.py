# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            n = q.popleft()
            if self.isSameTree(n,subRoot):
                return True
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return False

    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif (not p or not q) or(p.val!=q.val):
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)