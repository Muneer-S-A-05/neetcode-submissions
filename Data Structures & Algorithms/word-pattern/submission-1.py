class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s)!=len(pattern): return False

        smap = {}
        pmap = {}

        for i in range(len(s)):
            if s[i] in smap and smap[s[i]] != pattern[i]:
                return False
            if pattern[i] in pmap and pmap[pattern[i]] != s[i]:
                return False
            
            smap[s[i]] = pattern[i]
            pmap[pattern[i]] = s[i]

        return True