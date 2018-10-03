from collections import defaultdict
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.location = defaultdict(list)
        
        for i in range(len(nums)):
            self.location[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.location[target][random.randint(0, len(self.location[target]) - 1)]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
