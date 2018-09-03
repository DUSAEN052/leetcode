# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            left = self.minDepth(root.left) + 1
            right = self.minDepth(root.right) + 1
            
            if not root.left and root.right:
                return right
            elif not root.right and root.left:
                return left
            else:
                return min(left, right)
