class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        partial = []
        def dfs(i):
            if i>= len(nums):
                res.append(partial.copy())
                return
            
            # considering path taking x
            partial.append(nums[i])
            dfs(i+1)

            # considering path not taking x
            partial.pop()
            # skipping duplicate x since we this is not taking x path 
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res