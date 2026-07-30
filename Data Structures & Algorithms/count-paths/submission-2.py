class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * m

        for i in range(n-1):
            newRow = [1] * m
            for j in range(m-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]