class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        points = set()
        
        # function checks for word starting from given point only
        def dfs(r,c,next):
            # word found
            if next==len(word):
                return True
                
            #next is not matched
            if r<0 or c<0 or r>= len(board) or c>=len(board[0]) or word[next] != board[r][c] or (r,c) in points:
                return False

            # next is matched
            points.add((r,c))
            res = dfs(r+1,c,next+1) or dfs(r-1,c,next+1) or dfs(r,c+1,next+1) or dfs(r,c-1,next+1)
            points.remove((r,c))
            return res

        # running function starting from every point on the board
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        
        # if search failed
        return False