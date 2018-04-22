# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findDepth(root):
            if not root:
                return 0
            
            return 1 + max(findDepth(root.left), findDepth(root.right))
        
        return findDepth(root)
