# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        total = 0
        def check(node):
            nonlocal total
            if not node:
                return -1
            l = check(node.left)
            if l != -1:
                return l
            total += 1
            if total == k:
                return node.val
            r = check(node.right)
            if r != -1:
                return r
            return -1
            
        return check(root)