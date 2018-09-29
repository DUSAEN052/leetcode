# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = self.inorder(root)[::-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        
    
    def inorder(self, root):
        if root:
            root.left = self.inorder(root.left)
            root.right = self.inorder(root.right)
            
            return root.left + [root.val] + root.right
        return []

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
