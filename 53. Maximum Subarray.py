class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        max_sub = nums[0]
        
        for i in range(len(nums)):
            if nums[i] > total + nums[i]:
                total = nums[i]
            else:
                total += nums[i]
            
            max_sub = max(max_sub, total)
        
        return max_sub
