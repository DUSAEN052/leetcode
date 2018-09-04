class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedList = sorted(nums)
        endProd = sortedList[-1] * sortedList[-2] * sortedList[-3]
        startProd = sortedList[0] * sortedList[1] * sortedList[-1]
        
        return max(endProd, startProd)
