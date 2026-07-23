class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for x in nums:
            if x==0:
                curMax, curMin = 1, 1
                continue
            
            temp = curMax * x
            curMax = max(temp, curMin*x, x)
            curMin = min(temp, curMin*x, x)
            res = max(res,curMax)
        
        return res