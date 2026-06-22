class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        partial = []
        def dfs(arr):
            if not arr:
                res.append(partial.copy())
                return
            
            for i in range(len(arr)):
                partial.append(arr.pop(i))     
                dfs(arr)
                arr.insert(i,partial.pop())
        dfs(nums.copy())
        return res