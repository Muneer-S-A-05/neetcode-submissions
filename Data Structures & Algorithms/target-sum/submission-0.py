class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}

        def dfs(i,partial):

            if i>=len(nums):
                return 1 if partial==target else 0

            if (i,partial) in dp:
                return dp[(i,partial)]
            
            dp[(i,partial)] = dfs(i+1,partial+nums[i]) + dfs(i+1,partial-nums[i])
            return dp[(i,partial)]
        
        return dfs(0,0)
            