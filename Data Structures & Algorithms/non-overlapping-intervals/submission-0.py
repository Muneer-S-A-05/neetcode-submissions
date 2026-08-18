class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        r = intervals[0][0] - 1

        for s,e in intervals:
            if s<r:
                res += 1
                r = min(r,e)
            else:
                r = e
        
        return res