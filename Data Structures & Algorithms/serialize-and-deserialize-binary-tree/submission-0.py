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
        l = data[1:].split('#')
        if l[0]=='null': return None
        res = None
        def dfs(node):
            if not l:
                return None
            v = l.pop(0)
            v = None if v in ['null'] else int(v)
            if v:
                node = TreeNode(v)
                node.left=dfs(node.left)
                node.right=dfs(node.right)
                return node
            return None
        return dfs(res)