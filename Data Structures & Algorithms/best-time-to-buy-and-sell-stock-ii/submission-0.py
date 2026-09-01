class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curmin = prices[0]
        curmax = prices[0]
        for price in prices:
            if price<curmax:
                res += (curmax-curmin)
                curmin = curmax = price
            if price>curmax: curmax = price
            if price<curmin: curmin = price
        res += curmax-curmin
        return res