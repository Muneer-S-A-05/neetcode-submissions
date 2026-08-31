class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k!=0:
            nums[:k],nums[k:]=nums[n-k:],nums[:n-k]