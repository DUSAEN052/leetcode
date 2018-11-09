# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def bst(inpt, start, end):
            if start > end:
                return None
            
            middle = (start + end) // 2
            node = TreeNode(inpt[middle])
            node.left = bst(inpt, start, middle - 1)
            node.right = bst(inpt, middle + 1, end)
            
            return node
            
        if not nums:
            return None
        
        return bst(nums, 0, len(nums) - 1)
