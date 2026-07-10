class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        # we map node:[cost,nextNode] in hash set
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        # prims algo
        res = 0
        visit = set()
        heap = [[0,0]] # [cost,node], initially 0,0 at starting point
        while len(visit) < n:
            cost,i = heapq.heappop(heap)
            # we take min cost one and skip if node is already visited
            if i in visit:
                continue
            res += cost
            visit.add(i)
            # if not visited, its shortest path, we add it and then add its neighbours
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(heap,[neiCost,nei])
        
        return res