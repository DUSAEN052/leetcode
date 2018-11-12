class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        product = 1
        
        for i in range(1, len(nums)):
            output.append(output[i - 1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            output[i] *= product
        
        return output
