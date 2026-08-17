class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        l,r = intervals[0]
        for s,e in intervals[1:]:
            if s<=r:
                r = max(r,e)
            else:
                res.append([l,r])
                l,r = s,e
        res.append([l,r])
        return res