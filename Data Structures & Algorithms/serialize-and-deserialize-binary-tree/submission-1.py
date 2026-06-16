# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ''
        def dfs(node):
            if not node:
                self.s+='#null'
                return
            self.s+= '#'+str(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return(self.s)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = iter(data[1:].split('#'))
        def dfs(node):
            v = next(l)
            if v=='null':
                return None
            node = TreeNode(v)
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            return node
        return dfs(root)