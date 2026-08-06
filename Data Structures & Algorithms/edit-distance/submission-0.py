class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)==0:
            return len(word2)
        if len(word2)==0:
            return len(word1)

        if len(word1)<len(word2):
            word1,word2 = word2,word1
        below = [i for i in range(len(word2),-1,-1)]

        for i in range(len(word1)-1,-1,-1):
            curr = [0] * (len(word2)+1)
            curr[len(word2)] = len(word1)-i
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    curr[j] = below[j+1]
                else:
                    # below[j] means deletion
                    # curr[j+1] indicates insertion
                    # below[j+1] indicates replacement
                    curr[j] = 1+min(below[j],curr[j+1],below[j+1])
            below = curr

        return curr[0]