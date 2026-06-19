class MedianFinder:

    def __init__(self):
        self.n = 0
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        # adding to heap
        heapq.heappush(self.smallHeap,-num)
        heapq.heappush(self.bigHeap,-heapq.heappop(self.smallHeap))

        # checking for imbalance
        if len(self.smallHeap)<len(self.bigHeap):
            heapq.heappush(self.smallHeap,-heapq.heappop(self.bigHeap))


    def findMedian(self) -> float:
        if len(self.smallHeap)==len(self.bigHeap): # even no of elements
            return (self.bigHeap[0]-self.smallHeap[0])/2
        return -self.smallHeap[0]/1 # odd no of elements
        