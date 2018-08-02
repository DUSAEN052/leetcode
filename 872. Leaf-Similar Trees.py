# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(root):
            if root:
                if not root.left and not root.right:
                    return [root.val]
                
                return getLeaves(root.left) + getLeaves(root.right)   
            
            return []

        return getLeaves(root1) == getLeaves(root2)
