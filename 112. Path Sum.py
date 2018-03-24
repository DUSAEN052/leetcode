# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def checkTree(root, curr, target):
            if not root:
                return False
            elif not root.left and not root.right and root.val + curr == target:
                return True
            curr += root.val
            return checkTree(root.left, curr, target) or checkTree(root.right, curr, target)
        
        return checkTree(root, 0, sum)
