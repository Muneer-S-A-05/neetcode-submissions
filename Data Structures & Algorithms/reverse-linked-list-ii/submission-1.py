# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        empty = ListNode()
        empty.next = head
        
        cur = empty # left node
        pre = None # previous node before reversing range
        for _ in range(left):
            pre = cur
            cur = cur.next
        
        p = None # previous node for reversing range
        first = cur
        for _ in range(right-left+1):
            next = cur.next
            cur.next = p
            pre.next = cur
            p = cur
            cur = next

        first.next= cur

        return empty.next