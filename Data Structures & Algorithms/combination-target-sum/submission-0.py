class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        partial = []
        def dfs(i):
            if sum(partial)>target:
                return
            elif sum(partial)==target:
                # send in a copy or reference will be sent which gets updated
                res.append(partial.copy())
                return
            
            if i==len(nums):
                return

            partial.append(nums[i])
            dfs(i)

            partial.pop()
            dfs(i+1)

        dfs(0)
        return res