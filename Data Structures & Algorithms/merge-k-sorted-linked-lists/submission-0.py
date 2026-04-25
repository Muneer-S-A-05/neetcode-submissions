# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        # we update lists at each level of merge
        # so if len(lists) is 1, sorting done
        while len(lists) > 1:
            mergedlists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                # adding each sorted list header to mergelists
                mergedlists.append(self.merge(l1,l2))
            lists=mergedlists
        return lists[0]
    
    # good old 2 way sorting
    def merge(self,l1,l2):
        dummy = ListNode()
        temp = dummy
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1:
            temp.next=l1
        elif l2:
            temp.next=l2
        return dummy.next