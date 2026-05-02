class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h={}
        l={}
        n=len(prices)
        m=0
        for i,e in enumerate(prices):
            if i==0:
                l[i]=e
                h[n-1]=prices[n-1]
                continue
            l[i] = min (l[i-1],e)
            h[n-1-i] = max(h[n-i],prices[n-1-i])
        for i in range(n):
            m = max(m,h[i]-l[i])
        return m