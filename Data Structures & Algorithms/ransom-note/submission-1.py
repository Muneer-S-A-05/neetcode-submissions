class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = [0] * 26
        for m in magazine:
            counter[ord(m)-97] += 1
        for x in ransomNote:
            counter[ord(x)-97] -= 1
            if counter[ord(x)-97] < 0:
                return False
        return True