# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output = []
        q = [root]
        
        while q:
            output.append(q[-1].val)
            tmp = []
            
            while q:
                node = q.pop(0)
                
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        
        return output
