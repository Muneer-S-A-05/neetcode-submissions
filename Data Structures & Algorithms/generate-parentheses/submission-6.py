class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opened,closed,partial):
            if opened==n:
                if closed<n: # closing unclosed ones
                    partial += ')'*(n-closed)
                res.append(partial)
                return

            dfs(opened+1,closed,partial+'(') # new parentheses opened

            if opened>closed:
                dfs(opened,closed+1,partial+')') # parentheses closed

        dfs(0,0,'')
        return res