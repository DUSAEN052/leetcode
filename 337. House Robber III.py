# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def loot(root, hm):
            left, right, total = 0, 0, 0
            
            if not root:
                return 0
            elif root in hm:
                return hm[root]

            robbed = loot(root.left, hm) + loot(root.right, hm)
            if root.left:
                left = loot(root.left.left, hm) + loot(root.left.right, hm)
            if root.right:
                right = loot(root.right.left, hm) + loot(root.right.right, hm)
                
            notrobbed = left + right + root.val
            total = max(robbed, notrobbed)
            hm[root] = total
            
            return total
        
        return loot(root, {})
