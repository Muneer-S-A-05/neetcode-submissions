class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a,b = heapq.heappop(heap),heapq.heappop(heap)
            if a!=b:
                heapq.heappush(heap,-abs(a-b))
        return -heap[0] if heap else 0