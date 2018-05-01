# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q1, q2, output = [], [], []
        
        if not root:
            return root
        
        q1.append(root)
        output.append(root.val)
        
        while q1 or q2:
            while q1:
                if q1[0].left:
                    q2.append(q1[0].left)
                if q1[0].right:
                    q2.append(q1[0].right)
                q1.pop(0)
            
            if q2:
                output.append(sum(node.val for node in q2) / len(q2))
            
            while q2:
                if q2[0].left:
                    q1.append(q2[0].left)
                if q2[0].right:
                    q1.append(q2[0].right)
                q2.pop(0)
            
            if q1:
                output.append(sum(node.val for node in q1) / len(q1))
        
        return output
