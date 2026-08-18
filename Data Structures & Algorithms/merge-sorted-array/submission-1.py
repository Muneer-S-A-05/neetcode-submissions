class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r = m+n-1
        m-=1
        n-=1
        while m>-1 and n>-1:
            if nums1[m]>nums2[n]:
                nums1[r] = nums1[m]
                m-=1
            else:
                nums1[r] =nums2[n]
                n-=1
            r-=1
        while r > -1 and n>-1:
            nums1[r] = nums2[n]
            n-=1
            r-=1
        print(nums1)