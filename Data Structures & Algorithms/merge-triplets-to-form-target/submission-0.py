class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [0,0,0]

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            good = [max(good[i],t[i]) for i in range(3)]
            if good==target: return True

        return False