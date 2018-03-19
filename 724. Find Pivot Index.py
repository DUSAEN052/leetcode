class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            if total - left - nums[i] == left:
                return i
            left += nums[i]
        return -1
