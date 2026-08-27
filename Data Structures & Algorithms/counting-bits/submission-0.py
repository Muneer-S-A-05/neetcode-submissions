class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        curr = 1 # current msb 

        for i in range(1,n+1):
            if curr*2 == i:
                curr = i
            dp[i] = 1 + dp[i-curr]
        
        return dp