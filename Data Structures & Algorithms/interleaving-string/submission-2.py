class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3): return False
        dp = [False for j in range(len(s2)+1)]
        dp[len(s2)] = True

        for i in range(len(s1),-1,-1):
            newdp = [False for j in range(len(s2)+1)]
            for j in range(len(s2),-1,-1):
                if i==len(s1) and j==len(s2):
                    newdp[j] = True
                if i<len(s1) and s1[i]==s3[i+j] and dp[j]:
                    newdp[j] = True
                if j<len(s2) and s2[j]==s3[i+j] and newdp[j+1]:
                    newdp[j] = True
            dp = newdp

        return dp[0]