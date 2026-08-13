class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = Counter(hand)
        hand = sorted(list(set(hand)))
        i = 0

        while i<len(hand):
            temp = i+groupSize
            for j in range(groupSize-1,-1,-1):
                if d[hand[i]+j] < 1:
                    return False
                d[hand[i]+j] -= 1
                if d[hand[i]+j] > 0:
                    temp = i+j
            i = temp
        return True