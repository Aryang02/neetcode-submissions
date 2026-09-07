# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def finder(node):
            if not node:
                return 0, 0
            lh, ld = finder(node.left)
            rh, rd = finder(node.right)
            h = max(lh, rh) + 1
            d = max(ld, rd, lh+rh)
            return h, d
        
        return finder(root)[1]