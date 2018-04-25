class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1, t2):
            if t1 and t2:
                output = TreeNode(t1.val + t2.val)
                output.left = merge(t1.left, t2.left)
                output.right = merge(t1.right, t2.right)
                
                return output
            else:
                return t1 or t2
        
        return merge(t1, t2)
