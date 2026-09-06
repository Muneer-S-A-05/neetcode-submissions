class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [''] * numRows

        i = 0
        while i<len(s):
            for j in range(numRows):
                if i<len(s):
                    res[j] += s[i]
                    i += 1
            for j in range(numRows-2,0,-1):
                if i<len(s):
                    res[j] += s[i]
                    i += 1
        
        return ''.join(res)