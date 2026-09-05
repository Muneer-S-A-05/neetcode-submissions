class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for x in strs[1:]:
                if i>=len(x) or x[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]