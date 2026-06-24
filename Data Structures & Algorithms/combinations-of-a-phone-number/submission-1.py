class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return [] # incase input empty
        converts = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res = []

        def dfs(i,partial):
            if i>=len(digits):
                res.append(partial)
                return
            for x in converts[digits[i]]:
                dfs(i+1,partial+x)
            
        dfs(0,'')
        return res