class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def depth(root):
            if root:
                return 1 + max(depth(root.left), depth(root.right))
            return 0
        
        def plot(root, output, row, left, right):
            if root:
                col = (left + right) // 2
                output[row][col] = str(root.val)
                plot(root.left, output, row + 1,  left, col)
                plot(root.right, output, row + 1, col + 1, right)
        
        dep = depth(root)
        output = [["" for i in range((2 ** dep) - 1)] for k in range(dep)]
        plot(root, output, 0, 0, (2 ** dep) - 1)
        
        return output
