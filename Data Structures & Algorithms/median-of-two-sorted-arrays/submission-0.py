class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        # complexity will be defined by a, the smaller list
        if len(a)>len(b): a,b=b,a
        total=len(nums1)+len(nums2)
        half = total//2

        l,r=0,len(a)-1
        while True:
            # Left of a
            i = (r+l)//2
            # Left of b. Subracting 2 as we need index
            j = half-i-2

            # if i is negative we assume its -inf
            # this happens when that list isnt part of left partition
            am = a[i] if i>=0 else float("-infinity")
            bm = b[j] if j>=0 else float("-infinity")
            # if i if greater than list we assume inf
            # this happens when whole list is part of left partition
            anext = a[i+1] if (i+1) < len(a) else float("infinity")
            bnext = b[j+1] if (j+1) < len(b) else float("infinity")

            # we got the partition right
            if am<=bnext and bm<=anext:
                if total%2==1:
                    return min(anext,bnext)/1
                else:
                    return (max(am,bm)+min(anext,bnext))/2
            elif am>bnext:
                # too many elements from a
                r=i-1
            else:
                # too many elements from b
                l=i+1