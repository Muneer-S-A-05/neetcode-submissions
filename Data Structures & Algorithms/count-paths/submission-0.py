class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m+n<3 or m<2 or n<2:
            return 1

        res = 0
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 0
        for i in range(n+1):
            dp[m][i] = 0
        dp[m-1][n-1] = 1
        
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        return dp[0][0]