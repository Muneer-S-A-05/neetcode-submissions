class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and nums[i-1]==n:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                k= nums[l]+nums[r]+n
                if k>0:
                    r-=1
                elif k<0:
                    l+=1
                else:
                    p=[n,nums[l],nums[r]]
                    if p not in s:
                        s.append(p)
                    l+=1
                    r-=1
        return s
                