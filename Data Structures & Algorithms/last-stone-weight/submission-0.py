class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a,b = heapq.heappop(heap),heapq.heappop(heap)
            if a==b:
                if len(heap)==0:
                    return 0
            else:
                heapq.heappush(heap,-abs(a-b))
        return -heap[0]