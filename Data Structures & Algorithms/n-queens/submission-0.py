class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # for positive diags, the r+c value is same
        # for negative diags, the r-c value is same
        cols,posd,negd=set(),set(),set()
        partial = []
        def dfs(i):
            if i==n:
                res.append(partial.copy())
                return
            for j in range(n):
                if j not in cols and i+j not in posd and i-j not in negd:
                    partial.append('.'*j + 'Q' + '.'*(n-j-1))
                    cols.add(j)
                    posd.add(i+j)
                    negd.add(i-j)
                    dfs(i+1)
                    partial.pop()
                    cols.remove(j)
                    posd.remove(i+j)
                    negd.remove(i-j)
        
        dfs(0)
        return res