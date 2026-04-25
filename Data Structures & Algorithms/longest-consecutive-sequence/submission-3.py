class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        m=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                l=1
                while i+l in nums:
                    l+=1
                m= max(l,m)
        return m
