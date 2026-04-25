class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k=[]
        x,n=1,len(nums)
        for i in range(n):
            for j in range(n):
                x *= nums[j] if i!=j else 1
            k.append(x)
            x=1
        return k