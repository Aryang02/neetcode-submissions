# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p, q = dummy, dummy
        for _ in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next        
        return dummy.next
