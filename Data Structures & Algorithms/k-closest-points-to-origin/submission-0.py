class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distToOrigin(x,y):
            # not taking square root to make math simpler
            return (x**2 + y**2)
        # storing in negative to get max heap
        heap = [(-distToOrigin(i[0],i[1]),i[0],i[1]) for i in points]
        heapq.heapify(heap)
        # removing not top k points
        while len(heap)>k:
            heapq.heappop(heap)
        return [ [i[1],i[2]] for i in heap ]