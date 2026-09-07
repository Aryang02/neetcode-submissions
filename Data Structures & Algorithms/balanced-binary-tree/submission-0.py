# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0, True
            lh, la = helper(node.left)
            rh, ra = helper(node.right)
            h = 1 + max(lh, rh)
            if not la or not ra:
                return h, False
            if abs(lh-rh)>1:
                return h, False
            return h, True
        return helper(root)[1]