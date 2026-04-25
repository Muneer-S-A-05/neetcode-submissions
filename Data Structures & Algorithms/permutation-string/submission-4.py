class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=r=0
        ds1={}
        for i in s1:
            ds1[i]=ds1.get(i,0)+1
        ds2={}
        while r<len(s1):
            ds2[s2[r]] = ds2.get(s2[r],0)+1
            r+=1
        r-=1
        while r<len(s2)-1:
            if ds1==ds2:
                return True
            ds2[s2[l]] = ds2.get(s2[l],0)-1
            if ds2[s2[l]]==0:
                ds2.pop(s2[l])
            l+=1
            r+=1
            ds2[s2[r]] = ds2.get(s2[r],0)+1
        if ds1==ds2:
            return True
        return False