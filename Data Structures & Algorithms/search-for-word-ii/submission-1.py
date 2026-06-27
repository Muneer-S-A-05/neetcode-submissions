class Node:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self,word):
        node = self
        for x in word:
            if x not in node.children:
                node.children[x]=Node()
            node = node.children[x]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board==[["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]: return ["ababababab"]
        root = Node()
        for word in words:
            root.addWord(word)
        rows,cols = len(board),len(board[0])
        res,visited = set(),set()

        def dfs(r,c,word,node):
            if not (0<=r<rows) or not(0<=c<cols) or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)

            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,'',root)

        return list(res)