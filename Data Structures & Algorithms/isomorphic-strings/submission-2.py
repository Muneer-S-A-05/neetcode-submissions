class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        hashmap = {}

        s = s.lower()
        t = t.lower()

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                hashmap[s[i]] = t[i]
        
        return len(set(s)) == len(set(t))