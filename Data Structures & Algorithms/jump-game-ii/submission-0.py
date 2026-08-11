class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        dp = [0] * len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=len(nums)-1:
                dp[i] = 1
                continue
            if nums[i]==0:
                dp[i] = float('inf')
                continue
            dp[i] = min(dp[i+1:i+nums[i]+1]) + 1

        print(dp)        
        return dp[0]