class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]==target:
                return True
            elif matrix[m][0]>target:
                r=m-1
            else:
                l=m+1
        x=matrix[r]
        if r<0: return False
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