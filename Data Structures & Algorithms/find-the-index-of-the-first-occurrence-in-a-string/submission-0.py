class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        i,j = 0,0
        while i<len(haystack):
            if j==len(needle):
                return start
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=0
                start+=1
                i=start
        if j==len(needle):
            return start
        else:
            return -1