class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(list(set(nums)))
        
        if len(sort_nums) < 3:
            return sort_nums[-1]
        
        return sort_nums[-3]
