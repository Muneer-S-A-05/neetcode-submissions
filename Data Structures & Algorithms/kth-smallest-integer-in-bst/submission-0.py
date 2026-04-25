# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c=[0]
        def dfs(node):
            if not node:
                return 0
            print(c[0],node.val)
            if not node.left:
                c[0]+=1
                if c[0] == k:
                    c.append(node.val)
                    return 1
                else:
                    dfs(node.right)
            else:
                if not dfs(node.left):
                    c[0]+=1
                    if c[0]==k:
                        c.append(node.val)
                        return 1
                    else:
                        dfs(node.right)

        dfs(root)
        return c[1]