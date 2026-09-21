# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        flag = 1
        while queue:
            l = len(queue)
            temp = []
            queue.reverse()
            for i in range(l):
                node = queue.popleft()
                temp.append(node.val)
                if flag:
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                else:
                    if node.right: queue.append(node.right)
                    if node.left: queue.append(node.left)
            flag = 0 if flag else 1
            res.append(temp)
        return res