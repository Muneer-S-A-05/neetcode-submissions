class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x,n=1,len(nums)
        k=[1]*n
        l=[1]*n
        for i in range(n-1):
            m=1
            for j in range(i+1):
                m*= nums[j]
            k[i+1]=m
        for i in range(n):
            m=1
            for j in range(n-i,n):
                m*=nums[j]
            k[n-i-1]*=m
        return k           