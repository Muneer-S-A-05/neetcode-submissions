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
        while temp1 and temp2:
            k = temp1.val+temp2.val+remainder
            temp.next = ListNode(k%10)
            remainder = k//10
            temp,temp1,temp2 = temp.next,temp1.next,temp2.next
        while temp1:
            k = temp1.val+remainder
            temp.next = ListNode(k%10)
            remainder = k//10
            temp,temp1 = temp.next,temp1.next
        while temp2:
            k = temp2.val+remainder
            temp.next = ListNode(k%10)
            remainder = k//10
            temp,temp2 = temp.next,temp2.next
        if remainder>0:
            temp.next = ListNode(remainder)
        return dummy.next