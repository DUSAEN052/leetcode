class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        numbers = set(nums)
        
        return [i for i in range(1, len(nums) + 1) if i not in numbers]
