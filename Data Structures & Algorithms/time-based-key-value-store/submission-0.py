class TimeMap:
    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key] = self.d.get(key,[])+[(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        y= self.d.get(key,None)
        res=['',0]
        if y:
            for i,t in y:
                if t<=timestamp and t>res[1]:
                    res=[i,t]
        return res[0]