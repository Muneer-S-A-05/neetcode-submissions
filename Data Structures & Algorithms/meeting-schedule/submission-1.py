"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x:x.start)
        last = intervals[0].end
        for t in intervals[1:]:
            if t.start<last:
                return False
            last = t.end
        return True