class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True

        partial = []
        def dfs(i):
            # reached end means no issues, so palindrome partioning complete
            if i>=len(s):
                res.append(partial.copy())
                return
            # checking all substring starting from i till j
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    partial.append(s[i:j+1])
                    dfs(j+1)
                    partial.pop()
        
        dfs(0)
        return res