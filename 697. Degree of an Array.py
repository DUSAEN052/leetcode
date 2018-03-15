class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        group = []
        c = collections.Counter(nums)
        modes = c.most_common()
        mode = modes[0][1]
        degrees = []
        
        for i in range(len(modes)):
            if modes[i][1] == mode:
                degrees.append(modes[i][0])
            else:
                break
        
        smallest = float("inf")
        
        for degree in degrees:
            i1 = nums.index(degree)
            i2 = len(nums) - 1 - nums[::-1].index(degree)
            length = i2 - i1 + 1
            smallest = min(smallest, length)
        
        return smallest
    