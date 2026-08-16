class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)<1:
            return [newInterval]

        l,r = newInterval[0],newInterval[1]
        
        i=0
        res = []

        while i<len(intervals):
            start,end = intervals[i]

            if end<l:
                i+=1
                res.append([start,end])
                continue
            if start>r:
                break
            l = min(l,start)
            r = max(r,end)
            i+=1

        res.append([l,r])
        
        for _ in range(i,len(intervals)):
            res.append(intervals[_])
        
        return res
