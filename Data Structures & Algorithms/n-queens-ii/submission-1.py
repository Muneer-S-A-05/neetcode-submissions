class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        # for positive diags, the r+c value is same
        # for negative diags, the r-c value is same
        cols,posd,negd=set(),set(),set()
        def dfs(i):
            if i==n:
                nonlocal res
                res += 1
                return
            for j in range(n):
                if j not in cols and i+j not in posd and i-j not in negd:
                    cols.add(j)
                    posd.add(i+j)
                    negd.add(i-j)
                    dfs(i+1)
                    cols.remove(j)
                    posd.remove(i+j)
                    negd.remove(i-j)
        
        dfs(0)
        return res