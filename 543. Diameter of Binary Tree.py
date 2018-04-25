# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def great(root):
            if not root:
                return 0
            left = great(root.left)
            right = great(root.right)
            self.greatest = max(self.greatest, left + right)
            
            return 1 + max(left, right)
        
        self.greatest = 0
        
        if not root:
            return 0
        
        great(root)
        
        return self.greatest
