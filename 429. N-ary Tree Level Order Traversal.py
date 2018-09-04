"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
                    
                    for children in node.children:
                        q2.append(children)
                q1 = q2
            
            return levels
        
        return bfs(root)
