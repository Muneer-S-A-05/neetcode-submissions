class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        rows,cols = len(matrix), len(matrix[0])
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        
        res = 1

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp [(i,j)] = 1
            neighbor_lengths = [0]
            for dr,dc in neighbors:
                nr,nc = i+dr,j+dc
                if (0<=nr<rows) and (0<=nc<cols) and matrix[i][j]<matrix[nr][nc]:
                    neighbor_lengths.append(dfs(nr,nc))
            dp[(i,j)] += max(neighbor_lengths)
            return dp[(i,j)]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j))

        return res
