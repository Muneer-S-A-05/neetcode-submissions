class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        res = 0
        end = len(nums)-1
        while nums[end] == val and end>-1:
            end-=1
        for i in range(len(nums)):
            if end>i and nums[i] == val:
                nums[i] = nums[end]
                nums[end] = val
                end -= 1
                while nums[end] == val and end>i:
                    end -= 1
            if end<i: break
            res += 1
        print(nums)
        return res
