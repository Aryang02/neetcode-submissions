# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def helper(node):
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            peak = node.val + left + right
            self.best = max(self.best, peak)

            return node.val + max(left, right)
        
        helper(root)
        return self.best
