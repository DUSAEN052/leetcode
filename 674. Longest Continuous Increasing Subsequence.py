class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 1
        size = 0
        
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] < nums[i + 1]:
                tmp += 1
            else:
                tmp = 1
            size = max(size, tmp)
        
        return size
