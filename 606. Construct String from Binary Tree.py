class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        output = []
        
        def iterate(root, output):
            if root:
                output.append(str(root.val))
                if root.left:
                    output.append('(')
                    iterate(root.left, output)
                    output.append(')')
                elif not root.left and root.right:
                    output.append('(')
                    output.append(')')
                if root.right:
                    output.append('(')
                    iterate(root.right, output)
                    output.append(')')
        iterate(t, output)
        str1 = ''.join(output)
        return str1
