class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        res = values[s[0]]
        for i in range(1,len(s)):
            if values[s[i]] > values[s[i-1]]:
                res -= 2*values[s[i-1]]
            res += values[s[i]]
        
        return res