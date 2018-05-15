class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        
        return num * (num + 1) // 2 - sum(nums)
