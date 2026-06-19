class MedianFinder:

    def __init__(self):
        self.n = 0
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        # adding to heap
        if len(self.smallHeap)==0:
            heapq.heappush(self.smallHeap,-num)
        elif -self.smallHeap[0]>num:
            heapq.heappush(self.smallHeap,-num)
        else:
            heapq.heappush(self.bigHeap,num)

        # matching length so top elements produces median
        if abs(len(self.smallHeap)-len(self.bigHeap))>1:
            if len(self.smallHeap)>len(self.bigHeap):
                heapq.heappush(self.bigHeap,-heapq.heappop(self.smallHeap))
            else:
                heapq.heappush(self.smallHeap,-heapq.heappop(self.bigHeap))


    def findMedian(self) -> float:
        if len(self.smallHeap)==len(self.bigHeap): # even elements
            return (self.bigHeap[0]-self.smallHeap[0])/2
        if len(self.smallHeap)>len(self.bigHeap):
            return -self.smallHeap[0]/1
        return self.bigHeap[0]/1
        