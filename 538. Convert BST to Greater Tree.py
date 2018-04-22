# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convert(root):
            if not root:
                return None
            convert(root.right)
            self.sm += root.val
            root.val = self.sm
            convert(root.left)
            return root
        
        self.sm = 0
        return convert(root)
