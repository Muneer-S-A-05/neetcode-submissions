class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        for i in range(len(s)-1,-1,-1):
            # code cant start with 0
            if s[i] == "0":
                dp[i] = 0
            # we take value of next as we can form diff variation only when double digits are possible
            else:
                dp[i] = dp[i+1]

            # checking if double digit is possible
            if ( i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456") ):
                # we add to the current single digit possible variations, the number of possibilites in the variations that can be formed when i and i+1 are taken as single number
                dp[i] += dp[i+2]

        return dp[0]