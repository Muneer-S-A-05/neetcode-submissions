class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        partial = []
        def dfs(i,total):
            if total>target:
                return
            elif total==target:
                # send in a copy or reference will be sent which gets updated
                res.append(partial.copy())
                return
            
            if i==len(nums):
                return

            partial.append(nums[i])
            total += nums[i]
            dfs(i,total)

            partial.pop()
            total -= nums[i]
            dfs(i+1,total)

        dfs(0,0)
        return res