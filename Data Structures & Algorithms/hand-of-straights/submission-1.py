class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = Counter(hand)
        heapq.heapify(hand)
        top = heapq.heappop(hand)

        while hand:
            for j in range(groupSize):
                if d[top+j] < 1:
                    return False
                d[top+j] -= 1
            while d[top]<1 and hand:
                top = heapq.heappop(hand)
        return True