# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p, q = l1, l2
        last = None

        while p and q:
            summ = p.val + q.val + carry
            carry = summ//10
            p.val = summ%10
            last = p
            p = p.next
            q = q.next
        
        while p:
            summ = p.val + carry
            carry = summ//10
            p.val = summ%10
            last = p
            p = p.next
        while q:
            summ = q.val + carry
            carry = summ//10
            q.val = summ%10
            last.next = q
            last = q
            q = q.next
        if carry:
            last.next = ListNode(carry)
        
        return l1
