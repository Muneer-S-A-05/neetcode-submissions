class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        m = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(m-1,-1,-1):
            newdp = [0] * (amount+1)
            newdp[0] = 1
            for a in range(1,amount+1):
                newdp[a] = dp[a]
                if a - coins[i] >=0:
                    newdp[a] += newdp[a-coins[i]]
            dp = newdp
        
        return dp[amount]