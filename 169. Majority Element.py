from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        
        for item in count:
            if count[item] > len(nums) // 2:
                return item
