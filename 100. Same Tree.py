# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and not q or q and not p:
            return False
        else:
            if p.val != q.val:
                return False
            
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            
            return left and right
