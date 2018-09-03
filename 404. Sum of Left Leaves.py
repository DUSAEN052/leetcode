# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        output = []
        
        def getLeft(root, left):
            if not root:
                return 0
            elif not root.left and not root.right and left:
                output.append(root.val)
            else:
                getLeft(root.left, True)
                getLeft(root.right, False)

        getLeft(root, False)
        return sum(output)
