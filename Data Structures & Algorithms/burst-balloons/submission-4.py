class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[left boundary][rgiht boundary]
        # instead of thinking what if we pop this element next,
        # we do what if we pop this element last.

        # nums[l-1]*nums[i]*nums[r+1] + dp[i+1][r] + dp[l][i-1]

        # theres n square subarrrays and we go through for all n elements
        # therefor n cube is time complexity

        nums = [1] + nums + [1]
        dp = {}

        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            res = 0
            for i in range(l,r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += dfs(l,i-1) + dfs(i+1,r)
                res = max(res,coins)
            dp[(l,r)] = res
            return res

        return dfs(1,len(nums)-2)