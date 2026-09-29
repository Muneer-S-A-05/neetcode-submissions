class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        def helper(leftBias):
            l,r = 0,len(nums)-1
            i = -1
            while l<=r:
                mid = (r+l)//2
                if nums[mid]>target:
                    r = mid-1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    i = mid
                    if leftBias:
                        r = mid-1 
                    else:
                        l = mid+1
            return i
        return [helper(True),helper(False)]