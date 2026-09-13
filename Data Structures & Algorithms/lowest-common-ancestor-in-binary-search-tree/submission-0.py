# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        def helper(node):
            if not node:
                return False, False
            
            left_p, left_q = helper(node.left)
            right_p, right_q = helper(node.right)

            found_p = left_p or right_p or node.val == p.val
            found_q = left_q or right_q or node.val == q.val

            if found_p and found_q and self.res is None:
                self.res = node
            
            return found_p, found_q
            
        helper(root)
        return self.res