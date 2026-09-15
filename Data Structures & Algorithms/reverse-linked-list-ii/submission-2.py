# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        cur = head # left node
        pre = dummy # previous node before reversing range
        for _ in range(left-1):
            pre = cur
            cur = cur.next
        
        p = None # previous node for reversing range
        for _ in range(right-left+1):
            next = cur.next
            cur.next = p
            p = cur
            cur = next

        pre.next.next = cur
        pre.next = p

        return dummy.next