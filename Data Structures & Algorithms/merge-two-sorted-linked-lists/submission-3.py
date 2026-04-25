# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        head = None
        if a and b:
            if a.val<b.val:
                head=a
                a=a.next if a.next else None
            else:
                head=b
                b = b.next if b.next else None
        elif a:
            head=a
            a=a.next if a.next else None
        elif b:
            head=b
            b = b.next if b.next else None
        c = head if head else None
        while a and b:
            if a.val < b.val:
                c.next = a
                c = a
                a = a.next if a.next else None
            else:
                c.next = b
                c = b
                b = b.next if b.next else None
        while a:
            c.next = a
            c = a
            a = a.next if a.next else None
        while b:
            c.next = b
            c = b
            b = b.next if b.next else None
        return head