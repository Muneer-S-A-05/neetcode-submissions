class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i:[] for i in range(numCourses)}
        for cou, pre in prerequisites:
            preMap[cou].append(pre)

        visit,cycle = set(),set()
        def dfs(cou):
            if cou in cycle: # marks visiting currently
                return False
            if cou in visit: # marks already visited
                return True
            
            cycle.add(cou)
            for pre in preMap[cou]:
                if not dfs(pre):
                    return False
            cycle.remove(cou)
            visit.add(cou)
            res.append(cou)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res