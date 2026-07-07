class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]

        def union(n1,n2):
            par1, par2 = find(n1), find(n2)
            if par1==par2:
                return False
            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]