class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        
        for i,v in enumerate(nums):
            df = target-v
            if df in d:
                return [d[df],i]
            d[v]=i
        return