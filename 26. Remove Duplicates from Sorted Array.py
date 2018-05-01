class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        
        while nums:
            try:
                if nums[i] == nums[i + 1]:
                    nums.pop(i + 1)
                else:
                    i += 1
            except IndexError:
                break
        
        return len(nums)
