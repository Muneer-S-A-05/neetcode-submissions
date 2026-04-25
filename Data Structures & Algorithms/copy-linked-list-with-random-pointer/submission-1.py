"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = []
        temp = head
        n = 0
        while temp:
            d.append(temp)
            temp = temp.next
            n += 1
        r = [Node(-1) for i in range(n)]
        for i in range(n):
            r[i].val = d[i].val
            r[i].next = r[i+1] if i+1 < n else None
            r[i].random = r[d.index(d[i].random)] if d[i].random else None
        return r[0] if r else None