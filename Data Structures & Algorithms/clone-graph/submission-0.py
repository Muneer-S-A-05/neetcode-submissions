"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        table = {}

        def clone(node):
            # returning clone node as its already made
            if node in table:
                return table[node]

            # creating clone node
            copy = Node(node.val)
            table[node] = copy
            for x in node.neighbors:
                # recursively creating neighbor nodes
                copy.neighbors.append(clone(x))
            # returning perfectly cloned node (with neigbors)
            return copy
        
        return clone(node)
            