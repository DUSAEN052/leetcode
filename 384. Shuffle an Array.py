from random import sample
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst = nums
        self.og = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.lst = self.og
        return self.lst
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        order = sample(range(0, len(self.lst)), len(self.lst))
        return [self.lst[num] for num in order]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
