class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = list(set(nums))
        sort_nums.sort()

        if len(sort_nums) < 3:
            return sort_nums[-1]
        
        return sort_nums[-3]
