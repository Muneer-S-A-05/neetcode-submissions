# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # the node before the node to be nuked
        back = dummy
        # the node that goes till the end and beyond
        front = head
        count = 0
        # finding right distance between pointers
        while count<n and front:
            front = front.next
            count+=1
        # actual finding of solulu
        while front:
            front=front.next
            back=back.next
        # nuking the node
        back.next=back.next.next
        return dummy.next
        