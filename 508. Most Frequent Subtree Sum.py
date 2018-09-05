# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict 
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def getSum(root):
            if not root:
                return 0
            
            curr = root.val
            left = getSum(root.left)
            right = getSum(root.right)
            total = curr + left + right
            freq[total] += 1
            
            return total
        
        freq = defaultdict(int)
        getSum(root)
        maxFreq = max([value for value in freq.values()])
        
        return [key for key in freq if freq[key] == maxFreq]
