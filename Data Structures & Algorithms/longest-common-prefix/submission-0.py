class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        def helper(x,y):
            s = ''
            for i in range(len(x)):
                if i>=len(y) or x[i]!=y[i]: break
                s += x[i]
            return s
        
        for x in strs[1:]:
            res = helper(res,x)
        
        return res