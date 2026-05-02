class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for x in s:
            d[x]+=1
        for y in t:
            d[y]-=1
        for i in d.values():
            if i!=0:
                return False
        return True