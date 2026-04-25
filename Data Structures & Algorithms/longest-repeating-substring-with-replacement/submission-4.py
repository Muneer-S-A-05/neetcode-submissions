class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        m=0
        l=0
        for h in range(len(s)):
            d[s[h]] = d.get(s[h],0)+1
            while (h-l+1)-max(d.values())>k:
                d[s[l]]-=1
                l+=1
            m=max(m,h-l+1)
        return m