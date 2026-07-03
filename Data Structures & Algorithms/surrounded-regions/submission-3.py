class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        notSurrounded = set()

        def dfs(r,c):
            if not(0<=r<rows) or not (0<=c<cols) or board[r][c]=="X" or (r,c) in notSurrounded:
                return
            notSurrounded.add((r,c))
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if (nr,nc) not in notSurrounded:
                    dfs(nr,nc)

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in notSurrounded:
                    board[r][c] = "X"

        print(notSurrounded)