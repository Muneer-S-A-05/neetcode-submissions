class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        biggestdiff = 0
        for i in prices:
            if i < smallest:
                smallest = i
            if i - smallest > biggestdiff:
                biggestdiff = i - smallest
        return biggestdiff