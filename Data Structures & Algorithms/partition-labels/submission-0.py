class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        calculated = set()
        ranges = []
        res = []
        l = 0

        while l<len(s):
            r = len(s)-1
            if s[l] in calculated:
                l+=1
                continue
            while r>=l:
                if s[r]==s[l]:
                    calculated.add(s[l])
                    ranges.append([l,r])
                    break
                r-=1
            l+=1
        
        curr = ranges[0]
        for i in range(1,len(ranges)):
            l,r = ranges[i]
            if l<curr[1]:
                curr[1]=max(curr[1],r)
            else:
                res.append(curr[1]-curr[0]+1)
                curr = ranges[i]
        
        res.append(curr[1]-curr[0]+1)

        return res