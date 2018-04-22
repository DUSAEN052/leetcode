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
            left = 1 + findDepth(root.left)
            right = 1 + findDepth(root.right)
            
            return max(left,right)
        
        return findDepth(root)
