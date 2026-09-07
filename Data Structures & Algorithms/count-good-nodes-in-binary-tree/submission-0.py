# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        ans = 0
        def dfs(node, curr):
            nonlocal ans
            if not node:
                return
            if node.val >= curr:
                ans += 1
            dfs(node.left, max(curr, node.val))
            dfs(node.right, max(curr, node.val))
            return
        dfs(root, root.val)
        return ans