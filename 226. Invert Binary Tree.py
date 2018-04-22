# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(root):
            if not root:
                return root
            tmp = root.left
            root.left = root.right
            root.right = tmp
            invert(root.left)
            invert(root.right)
            
            return root
        
        return invert(root)
