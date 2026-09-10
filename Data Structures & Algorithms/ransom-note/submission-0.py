class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for x in ransomNote:
            if x in c and c[x] > 0:
                c[x]-=1
            else:
                return False
        return True