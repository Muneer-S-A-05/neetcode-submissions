class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s if i.isalnum()]).lower()
        i,j=0,len(s)-1
        print(s)
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True