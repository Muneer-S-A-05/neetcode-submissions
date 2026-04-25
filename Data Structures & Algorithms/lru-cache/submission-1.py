class Node:
    def __init__(self,key,value):
        self.key,self.value=key,value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        # python's inbuilt collections.OrderedDict()
        self.cache=OrderedDict()
        self.cap=capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # making it the mru using move_to_end
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache)>self.cap:
            # popitem usually removes last added element
            # only last element can be removed in standard lib (lifo)
            self.cache.popitem(last=False)
        
