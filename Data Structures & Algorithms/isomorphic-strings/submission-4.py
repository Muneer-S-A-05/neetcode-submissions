class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        smap = {}
        tmap = {}

        for i in range(len(s)):
            if s[i] in smap and smap[s[i]] != t[i]:
                return False
            smap[s[i]] = t[i]

            if t[i] in tmap and tmap[t[i]] != s[i]:
                return False
            tmap[t[i]] = s[i]
        
        return True