class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(x,ans):
            if len(ans)==k:
                res.append(ans[:])
                return
            for i in range(x,n+1):
                dfs(i+1,ans+[i])
        dfs(1,[])
        return res
