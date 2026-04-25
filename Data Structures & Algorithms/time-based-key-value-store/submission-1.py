class TimeMap:
    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        y = self.d.get(key,None)
        if not y:
            return ""
        res=""
        l,r=0,len(y)-1
        while l <= r:
            m = (l+r)//2
            if y[m][1] <= timestamp:
                res = y[m][0]
                l = m+1
            else:
                r = m-1
        return res