class Solution:
    def trap(self, height: List[int]) -> int:
        maxl,maxr=height[0],height[-1]
        l,r=0,len(height)-1
        k=0
        while l<r:
            if maxl<=maxr:
                l+=1
                maxl=max(maxl,height[l])
                k+= maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                k+= maxr - height[r]
        return k
                