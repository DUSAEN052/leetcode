class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chase = nums[0]
        chaser = nums[nums[0]]
        
        while chase != chaser:
            chase = nums[chase]
            chaser = nums[nums[chaser]]
        
        chase = 0
        while chase != chaser:
            chase = nums[chase]
            chaser = nums[chaser]
        
        return chase
