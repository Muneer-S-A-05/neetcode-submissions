class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # making basic neighbour hashmap
        edgeMap = defaultdict(list)
        for u,v,t in times:
            edgeMap[u].append((v,t))
        
        # using minheap to select shortest time path bfs
        heap = [(0,k)]
        visited = set()
        t = 0

        while heap:
            time,node  = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,time)

            for node2,time2 in edgeMap[node]:
                if node2 not in visited:
                    heapq.heappush(heap,(time+time2,node2))
        
        return t if len(visited)==n else -1