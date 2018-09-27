# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def preorder(root):
            if root:
                output.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        output = []
        preorder(root)
        sortedOutput = sorted(output)
        
        return sortedOutput[k - 1]
