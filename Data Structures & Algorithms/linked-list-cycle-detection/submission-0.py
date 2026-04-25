# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp:
            if temp.val=='donkey':
                return True
            temp.val='donkey'
            temp=temp.next
        return False