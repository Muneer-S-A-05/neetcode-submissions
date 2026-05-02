class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda:-1)
        l=0
        m=0
        n=0
        for i,e in enumerate(s):
            if d[e]>-1 and d[e]>=l:
                print(d.keys(),d.values())
                m=max(m,n)
                n=i-d[e]
                l=d[e]
                print(i,n,l)
                d[e]=i
            else:
                d[e]=i
                n+=1
        m=max(m,n)
        return m