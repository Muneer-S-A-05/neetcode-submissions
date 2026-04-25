# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # i'll get 2 pointers
        # one stays at begin and other goes to kth node
        # then reverse node between first 2 nodes
        # repeat for the remaining nodes
        flag=0
        dummy = None
        left,right=head,head
        prev=None
        while right:
            # finding right limit
            for i in range(k-1):
                if right:
                    right=right.next
                else:
                    break
            # less than k nodes remaining case
            if not right: break
            # flag is used to get new head node and stored in dummy
            if not flag:
                    flag=1
                    dummy = right
            else:
                # attachment reversed list to next part
                oleft.next=right
            prev = right.next
            right = right.next
            # storing for next round
            oleft = left
            # reversing list
            while True:
                print(left.val,prev.val if prev else None)
                next = left.next
                left.next = prev
                prev=left
                left = next
                if next==right: break
        return dummy if flag else head
            
