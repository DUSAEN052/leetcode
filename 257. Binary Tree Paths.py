# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        output = []
        
        def findPath(root, path):
            if root:
                if not root.left and not root.right:
                    output.append(path + str(root.val))
                elif not root:
                    return None
                else:
                    findPath(root.left, path + str(root.val) + "->")
                    findPath(root.right, path + str(root.val) + "->")
        
        findPath(root, "")
        
        return output
