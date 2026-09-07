class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lps = [0] * len(needle)
        prevlps,i = 0,1

        while i < len(needle):
            if needle[i] == needle[prevlps]:
                prevlps += 1
                lps[i] = prevlps
                i += 1
            elif prevlps == 0:
                lps[i] = 0
                i += 1
            else:
                prevlps = lps[prevlps - 1]

        i,j = 0,0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            elif j==0:
                i += 1
            else:
                j = lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1