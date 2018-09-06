# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        
        if not root:
            return output
    
        q1 = [root]

        while q1:
            q2 = []
            output.append(max([node.val for node in q1]))

            for node in q1:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            q1 = q2
   
        return output
