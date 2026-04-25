class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = list(sorted(nums))
        m=0
        x=0
        for i in range(len(n)):
            if x>0:
                if n[i]==n[i-1]+1:
                    x+=1
                elif n[i]==n[i-1]:
                    continue
                else:
                    if x>m:
                        m=x
                    x=1
            else:
                x=1
        if x>m:
            m=x
        print(n)
        return m