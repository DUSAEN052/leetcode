# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        q1 = [root]
        
        while q1:
            q2 = []
            self.nodes.extend(q1)
            
            while q1:
                node = q1.pop(0)
                
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2

    
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.nodes[(len(self.nodes) - 1) // 2]
        node = TreeNode(v)
        
        if parent.left:
            parent.right = node
        else:
            parent.left = node
        
        self.nodes.append(node)
        return parent.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
