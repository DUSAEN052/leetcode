# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_val = -float('inf')
        min_val = float('inf')

        return self.dfs(root, max_val, min_val)

    def dfs(self, root, max_val, min_val):
        if root:
            maxv = max(max_val, root.val)
            minv = min(min_val, root.val)
            left = self.dfs(root.left, maxv, minv)
            right = self.dfs(root.right, maxv, minv)

            return max(left, right)
        return max_val - min_val
