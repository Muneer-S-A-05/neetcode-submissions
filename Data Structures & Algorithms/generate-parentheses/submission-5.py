class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []
        def dfs(i,partial):
            print(partial,stack)
            if i==n:
                if stack:
                    partial += ')'*len(stack)
                res.append(partial)
                return

            stack.append('(')
            dfs(i+1,partial+'(') # if new parentheses opened
            if stack:
                stack.pop()

            if stack:
                stack.pop()
                dfs(i,partial+')') # if closed
                stack.append('(') # if not closed

        dfs(0,'')
        return res