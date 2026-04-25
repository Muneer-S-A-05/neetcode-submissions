class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<2: return nums[0]
        res = nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<res:
                res=nums[m]
                r=m-1
            else:
                l=m+1
        return res