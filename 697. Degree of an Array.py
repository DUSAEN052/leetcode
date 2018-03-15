from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        modes = Counter(nums).most_common()
        mode = modes[0][1]
        degrees = []
        
        for m in modes:
            if m[1] == mode:
                degrees.append(m[0])
        
        smallest = float("inf")
        
        for degree in degrees:
            i1 = nums.index(degree)
            i2 = len(nums) - 1 - nums[::-1].index(degree)
            length = i2 - i1 + 1
            smallest = min(smallest, length)
        
        return smallest