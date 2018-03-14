# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        elements = []
        
        def getElements(root, elements):
            if root:
                elements.append(root.val)
                getElements(root.left, elements)
                getElements(root.right, elements)
        
        getElements(root, elements)
        smallest = float("inf")
        
        for i in range(len(elements)):
            for k in range(i + 1, len(elements)):
                smallest = min(smallest, abs(elements[k] - elements[i]))
        return smallest
