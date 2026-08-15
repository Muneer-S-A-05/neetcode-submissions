class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # stores the last occurence of each letter
        lastOccur = {c:i for i,c in enumerate(s)}

        res = []
        first=last = 0
        for i,c in enumerate(s):
            last = max(last,lastOccur[c])
            if i==last:
                res.append(last-first+1)
                first = i+1

        return res