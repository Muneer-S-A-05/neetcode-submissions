class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            mid = l + (r-l)//2 # to avoid overflow
            if mid>0 and nums[mid]<nums[mid-1]:
                r = mid-1
            elif mid<n-1 and nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                return mid