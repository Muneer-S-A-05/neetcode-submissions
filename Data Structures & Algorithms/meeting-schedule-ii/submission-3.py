"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        res = 0
        count = 0

        # we will check for max number of overlapping intervals
        start = sorted([t.start for t in intervals])
        end = sorted([t.end for t in intervals])

        i,j = 0,0 # pointers to start and end times

        while i<len(start) and j<len(end):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res,count)
        return res