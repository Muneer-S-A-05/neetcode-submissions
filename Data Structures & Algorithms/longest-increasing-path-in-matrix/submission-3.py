class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows,cols = len(matrix), len(matrix[0])
        dp = [[0 for j in range(cols)] for i in range(rows)]
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 1

        def dfs(i,j):
            if dp[i][j]>0:
                return dp[i][j]
            
            res = 1
            neighbor_lengths = [0]
            for dr,dc in neighbors:
                nr,nc = i+dr,j+dc
                if (0<=nr<rows) and (0<=nc<cols) and matrix[i][j]<matrix[nr][nc]:
                    res = max(res,1+dfs(nr,nc))
            dp[i][j] = res
            return res
        
        
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j))

        return res