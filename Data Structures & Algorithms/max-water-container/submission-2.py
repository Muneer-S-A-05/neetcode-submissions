class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        m=0
        while l<r:
            a = (r-l)*min(heights[l],heights[r])
            m=max(a,m)
            print(l,heights[l],r,heights[r],a)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1            
        return m