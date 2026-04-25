# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=l1,l2
        dummy = ListNode()
        temp = dummy
        remainder = 0
        while temp1 or temp2 or remainder:
            v1 = temp1.val if temp1 else 0
            v2 = temp2.val if temp2 else 0
            k = v1+v2+remainder
            temp.next = ListNode(k%10)
            remainder = k//10
            temp = temp.next
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        return dummy.next