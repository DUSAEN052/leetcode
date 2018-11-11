# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root):
            if not root:
                return []
            output = [root.val]
            output += preorder(root.left)
            output += preorder(root.right)
            
            return output
        
        return preorder(root)
