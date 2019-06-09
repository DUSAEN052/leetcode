# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    total = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return root
        
    def inorder(self, root):
        if root:
            self.inorder(root.right)
            tmp = root.val
            root.val += self.total
            self.total += tmp
            self.inorder(root.left)
