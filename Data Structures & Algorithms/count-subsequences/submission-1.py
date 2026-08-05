class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==len(s) or j==len(t):
                return 1 if j == len(t) else 0

            res = dfs(i+1,j)
            res += dfs(i+1,j+1) if s[i]==t[j] else 0
            dp[(i,j)] = res
            return res
        
        return dfs(0,0)