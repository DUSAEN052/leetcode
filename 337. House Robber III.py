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
            
            if root in hm:
                return hm[root]
            if root:
                robbed = loot(root.left, hm) + loot(root.right, hm)
                if root.left:
                    left = loot(root.left.left, hm) + loot(root.left.right, hm)
                if root.right:
                    right = loot(root.right.left, hm) + loot(root.right.right, hm)
                notrobbed = left + right + root.val
            elif not root:
                return 0
            
            total = max(robbed, notrobbed)
            hm[root] = total
            return total
        
        mem = {}
        money = loot(root, mem)
        
        return money
