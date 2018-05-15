class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        
        for i in range(len(nums)):
            if i not in n:
                return i
        
        return len(nums)
