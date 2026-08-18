class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorting by end values
        intervals.sort(key=lambda x:x[1])

        nonOverlapping = 0

        r = intervals[0][0] - 1

        for s,e in intervals:
            if s>=r:
                nonOverlapping += 1
                r = e
        return len(intervals)-nonOverlapping