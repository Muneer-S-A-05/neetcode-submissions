class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we use min heap of size k
        self.heap,self.k = nums, k
        heapq.heapify(self.heap)
        # pop elements that aren't in top k
        # works because we never remove element from heap
        # so lower elements will never be in top k
        # maintaining this will put kth element always at top
        while len(self.heap)>k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        # in case initially nums had less than k
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]