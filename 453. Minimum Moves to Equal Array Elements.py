class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ssmall = min(nums)
        output = 0        
            
        return sum([num - small for num in nums])
