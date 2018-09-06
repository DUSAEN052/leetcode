class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        
        for i in range(len(nums)):
            num = target - nums[i]
            
            if num in mapping:
                return [mapping[num], i]
            else:
                mapping[nums[i]] = i
