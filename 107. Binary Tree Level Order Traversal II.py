# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        def bfs(root):
            q1 = []
            q1.append(root)
            levels = []
            
            while q1:
                q2 = []
                levels.append([node.val for node in q1])
                
                while q1:
                    node = q1.pop(0)
                    
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
                
                q1 = q2
            
            return levels
        
        return(bfs(root)[::-1])
