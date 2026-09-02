class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap: return False
        self.hashMap[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap: return False
        index = self.hashMap[val]
        last = self.values[-1]
        self.values[index] = last
        self.values.pop()
        self.hashMap[last] = index
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()