class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = []
        count = 0
        
        for i, num in enumerate(nums):
            if nums[i] == 1:
                count += 1
            else:
                output.append(count)
                count = 0
        
        output.append(count)
        
        return max(output)
