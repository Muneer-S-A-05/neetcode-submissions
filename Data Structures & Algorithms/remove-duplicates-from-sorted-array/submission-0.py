class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i,j = 1,0
        while j<len(nums)-1:
            while j<len(nums)-1 and nums[j]==nums[j+1]:
                j += 1
            if j>len(nums)-2: break
            nums[i] = nums[j+1]
            i+=1
            j+=1
        return i