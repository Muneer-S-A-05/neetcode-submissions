class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k=[1]*n
        for i in range(n-1):
            k[i+1]=k[i]*nums[i]
        for i in range(n):
            if i==0:
                p=1
            else:
                p*=nums[n-i]
            k[n-i-1]*=p
        return k           