"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        p = head
        dummy = Node(0)
        q = dummy
        while p:
            new = Node(p.val, None, p.random)
            q.next = new
            q = q.next
            nodes[p] = q
            p = p.next
        q = dummy.next
        while q:
            if q.random in nodes:
                q.random = nodes[q.random]
            q = q.next
        return dummy.next
        