class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = sum(nums[:k])
        maxNum = total
        
        for i in range(len(nums) - k):
            total = total - nums[i] + nums[i + k]
            maxNum = max(maxNum, total)
        
        return maxNum / k
