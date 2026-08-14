class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False

        d = Counter(hand)
        
        for i in sorted(d):
            left = d[i]
            if left > 0:
                for j in range(i,i+groupSize):
                    if left > d[j]: return False
                    d[j] -= left
        
        return True