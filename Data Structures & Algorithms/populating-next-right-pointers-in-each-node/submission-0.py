"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        queue = deque()
        queue.append(root)

        while queue:
            children = []
            for _ in range(len(queue)):
                node = queue.popleft()
                node.next = queue[0] if queue else None
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            for child in children:
                queue.append(child)
        
        return root