class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        partial = []
        def dfs(arr):
            if not arr:
                res.append(partial.copy())
                return
            
            for i in range(len(arr)):
                partial.append(arr[i])     
                dfs(arr[:i]+arr[i+1:])
                partial.pop()
        dfs(nums.copy())
        return res