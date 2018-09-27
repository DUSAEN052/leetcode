# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if not root:
                return []
            
            return inorder(root.left) + [root.val] + inorder(root.right)

        nodes = inorder(root)
        tree = TreeNode(nodes.pop(0))
        prev = tree

        for node in nodes:
            tree.right = TreeNode(node)
            tree = tree.right

        return prev
