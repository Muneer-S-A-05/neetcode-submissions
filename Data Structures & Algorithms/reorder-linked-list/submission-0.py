# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        temp = head
        # takes O(n) time and space
        while temp:
            stack.append(temp)
            temp=temp.next
        l,r = 0,len(stack)-1
        while l<r:
            stack[r].next=stack[l].next
            stack[l].next=stack[r]
            l+=1
            r-=1
        # Choppping of tail
        stack[l].next=None