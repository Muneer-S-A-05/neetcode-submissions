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
        if not head: return None
        # using hashmap to map old node to new node
        d = {}
        # giving new node only val
        temp = head
        while temp:
            d[temp] = Node(temp.val)
            temp = temp.next
        # giving new node next and random
        temp = head
        while temp:
            d[temp].next = d.get(temp.next,None)
            d[temp].random = d.get(temp.random,None)
            temp = temp.next            
        return d[head]