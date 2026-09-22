class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vars = defaultdict(list)
        # a -> [b,a/b]

        for i,eq in enumerate(equations):
            x,y = eq
            vars[x].append([y,values[i]])
            vars[y].append([x,1/values[i]])
        
        def bfs(src,tar):
            if src not in vars or tar not in vars:
                return -1/1
            q,visited = deque([[src,1]]),set() # src, current product
            while q:
                n,w = q.popleft() # node,weight
                if n == tar:
                    return w
                for nei,weight in vars[n]:
                    if nei not in visited:
                        q.append([nei,weight*w])
                        visited.add(nei)
            return -1/1

        return [ bfs(src,tar) for src,tar in queries ]