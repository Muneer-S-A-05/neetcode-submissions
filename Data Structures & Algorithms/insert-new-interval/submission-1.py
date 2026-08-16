class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        l,r = newInterval

        for i in range(len(intervals)):
            start,end = intervals[i]
            if r < start:
                return res + [[l,r]] + intervals[i:]
            elif l > end:
                res.append(intervals[i])
            else:
                l,r = min(l,start),max(r,end)
        
        res.append([l,r])
        return res