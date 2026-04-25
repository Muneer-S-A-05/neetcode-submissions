class MinStack:

    def __init__(self):
        self.stack=[]
        self.minvalue=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minvalue:
            self.minvalue.append(min(val,self.minvalue[-1]))
        else:
            self.minvalue.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minvalue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvalue[-1]