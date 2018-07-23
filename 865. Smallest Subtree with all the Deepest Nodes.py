# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def depth(root, dep):
            if root:
                l = depth(root.left, dep + 1)
                r = depth(root.right, dep + 1)
                
                return max(l, r) + 1
            
            return 0
        
        def findtree(root, dep):
            if root:
                l = depth(root.left, dep + 1)
                r = depth(root.right, dep + 1)

                if l == r:
                    return root
                elif l > r:
                    return findtree(root.left, l)
                elif r > l:
                    return findtree(root.right, r)
            
            return root

        return findtree(root, 0)
