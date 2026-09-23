class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(ans,x):
            if len(ans)==k:
                res.append(ans)
                return
            if x>n:
                return
            dfs(ans,x+1)
            dfs(ans+[x],x+1)
        dfs([],1)
        return res