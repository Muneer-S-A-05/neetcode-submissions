# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        n, dummy = 0, ListNode(0,head)
        last = dummy
        while last.next:
            n,last = n+1,last.next

        k = k%n
        if not k:
            return head

        cut = dummy
        for i in range(n-k): cut = cut.next
        # cut points at last node of result

        last.next = head
        dummy.next = cut.next
        cut.next = None

        return dummy.next