# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        dummy = ListNode()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow
        while start:
            temp = start.next
            start.next = dummy.next
            dummy.next = start
            start = temp
        
        p, q = head, dummy.next
        while p is not q and q is not None and q.next is not p:
            p_next = p.next
            q_next = q.next
            p.next = q
            if p_next is not q:
                q.next = p_next
            p = p_next
            q = q_next
        