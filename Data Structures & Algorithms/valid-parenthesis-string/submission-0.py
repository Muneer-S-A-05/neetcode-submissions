class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0

        for x in s:
            
            if x=='(':
                leftmin+=1
                leftmax+=1
            elif x=='*':
                leftmin-=1
                leftmax+=1
            else:
                leftmin-=1
                leftmax-=1
            
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
            
        return leftmin==0
