class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # when we buy we got to next index
        # when we sell we skip the next index

        dp = {} # key is index and current state, value is max profit

        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            cooldown = dfs(i+1,buying)
            if buying:
                buyorsell = dfs(i+1,False) - prices[i]
            else:
                buyorsell = dfs(i+2,True) + prices[i]
            dp[(i,buying)] = max(buyorsell,cooldown)
            return dp[(i,buying)]
        
        return dfs(0,True)