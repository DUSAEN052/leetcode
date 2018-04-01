class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = nums[0]
        output = 0
        
        for num in nums:
            small = min(small, num)
            
        for num in nums:
            output += num - small
        
        return output
