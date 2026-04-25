class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        # hash maps
        ds1,ds2=[0]*26,[0]*26

        # recording info of s1 into hash maps
        for i in range(len(s1)):
            ds1[ord(s1[i])-ord('a')]+=1
            ds2[ord(s2[i])-ord('a')]+=1
        
        # comparing hash maps of s1 and s2
        # storing number of matched values in matched
        matched = 0
        for i in range(26):
            matched += (1 if ds1[i]==ds2[i] else 0)

        l=0
        for r in range(len(s1),len(s2)):
            if matched==26: return True

            # next right value
            i = ord(s2[r]) - ord('a')
            ds2[i]+=1
            if ds1[i]==ds2[i]: # if new right brings new match
                matched+=1
            elif ds1[i]+1==ds2[i]: # if new right loses exists match
                matched-=1
            
            j=ord(s2[l]) - ord('a')
            ds2[j]-=1
            if ds1[j]==ds2[j]: # if new left brings new match
                matched+=1
            elif ds1[j]-1==ds2[j]: # if new left loses exists match
                matched-=1

            l+=1
        return matched==26