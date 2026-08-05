class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i,partial):
            if (i,partial) in dp:
                return dp[(i,partial)]
            if i==len(s):
                return 1 if partial == t else 0
            
            if partial != t[:len(partial)]:
                return 0

            res = dfs(i+1,partial) + dfs(i+1,partial+s[i])
            dp[(i,partial)] = res
            return res
        
        return dfs(0,'')