class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        space = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                space += 1
            else:
                nums[i - space] = nums[i]
                if space != 0:
                    nums[i] = 0
