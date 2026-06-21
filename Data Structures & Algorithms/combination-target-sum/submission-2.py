class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        partial = []
        def dfs(i,total):
            if total==target:
                # send in a copy or reference will be sent which gets updated
                res.append(partial.copy())
                return
            if total>target or i>=len(nums):
                return

            partial.append(nums[i])
            dfs(i,total+nums[i])

            partial.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res