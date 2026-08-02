class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1 # partial sum to count

        for i in range(len(nums)):
            newdp = defaultdict(int)
            for partial,count in dp.items():
                newdp[partial+nums[i]] += count
                newdp[partial-nums[i]] += count
            dp = newdp
        
        return dp[target]