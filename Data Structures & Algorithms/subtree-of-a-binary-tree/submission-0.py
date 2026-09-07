# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        def check(node, subnode):
            if not node and not subnode:
                return True
            if node and not subnode or not node and subnode:
                return False
            a = check(node.left, subnode.left)
            b = check(node.right, subnode.right)
            if not a or not b:
                return False
            return True if node.val == subnode.val else False

        def traverse(node):
            nonlocal ans
            if not node:
                return
            if node.val == subRoot.val:
                ans = check(node, subRoot) or ans
            traverse(node.left)
            traverse(node.right)
            return

        traverse(root)
        return ans

        

