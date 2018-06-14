# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def prune(root):
            if not root:
                return root
            
            root.left = prune(root.left)
            root.right = prune(root.right)
            
            return root if root.val == 1 or root.left or root.right else None
        
        return prune(root)
