class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            if target<=x[-1] and target>=x[0]:
                if len(x)<2: return target==x[0]
                l,r=0,len(x)-1
                while l<=r:
                    m=(l+r)//2
                    if x[m]==target:
                        return True
                    elif x[m]>target:
                        r=m-1
                    else:
                        l=m+1
                return False
        return False