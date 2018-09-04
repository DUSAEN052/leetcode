# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(root):
            q1 = []
            q1.append(root)
            
            while q1:
                q2 = []
                
                while q1:
                    node = q1.pop(0)
                    output = node.val
                    
                    if node.right:
                        q2.append(node.right)
                    if node.left:
                        q2.append(node.left)
                q1 = q2
                
                if not q1:
                    return output    
        
        return bfs(root)
