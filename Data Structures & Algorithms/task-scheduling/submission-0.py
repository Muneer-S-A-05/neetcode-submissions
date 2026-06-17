class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap using in built function Counter
        count = Counter(tasks)
        # it doesn't matter what the value of letter is, so we only take value
        maxHeap = [-i for i in count.values()]
        # we take higher freq first to get min time
        heapq.heapify(maxHeap)
        
        time = 0
        # stores values removed from maxHeap, waiting for cooldown
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                c = heapq.heappop(maxHeap) + 1 # '+' cause we store as negative
                if c: # we don't wanna put it to heap it count is 0
                    q.append([c,time+n])
            #cooldown over
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time