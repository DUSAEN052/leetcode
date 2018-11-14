# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(root, L, R):
            if not root:
                return 0
            root_val = 0
            
            if root.val >= L and root.val <= R:
                root_val += root.val
            left = dfs(root.left, L, R)
            right = dfs(root.right, L, R)
            
            return root_val + left + right
        
        return dfs(root, L, R)
