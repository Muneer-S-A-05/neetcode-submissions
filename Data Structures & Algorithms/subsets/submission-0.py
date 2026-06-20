class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # to track current subset (curr node of tree)
        subset = []
        def dfs(i):
            # end node
            if i>=len(nums):
                res.append(subset.copy())
                return

            # when nums[i] is added path
            subset.append(nums[i])
            dfs(i+1)

            # when nums[i] is not added path
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res