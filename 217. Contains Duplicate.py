from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = Counter(nums)
        
        for num in mp:
            if mp[num] != 1:
                return True
        
        return False
