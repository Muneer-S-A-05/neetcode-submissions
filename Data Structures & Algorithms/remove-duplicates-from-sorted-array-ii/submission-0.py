class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,0
        while j<len(nums):
            count = 1
            while j+1<len(nums) and nums[j]==nums[j+1]:
               j+=1
               count+=1
            for x in range(min(2,count)):
                nums[i]=nums[j]
                i+=1
            j+=1
        return i