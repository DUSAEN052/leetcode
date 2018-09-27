# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        def tree(N):
            if N == 1:
                return [TreeNode(0)]
            
            output = []
            
            for i in range(1, N, 2):
                for left in tree(i):
                    for right in tree(N - i - 1):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        output.append(node)
            
            return output
        
        if N % 2 == 0:
            return []
        
        return tree(N)
