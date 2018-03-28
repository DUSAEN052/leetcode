class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a1 = nums[:]
        a2 = nums[:]
        boolean1 = True
        boolean2 = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                a1[i] = nums[i + 1]
                a2[i + 1] = nums[i]
                break

        for j in range(len(a1) - 1):
            if a1[j] > a1[j + 1]:
                boolean1 = False
                break
        
        for k in range(len(a2) - 1):
            if a2[k] > a2[k + 1]:
                boolean2 = False
                break
        
        return boolean1 or boolean2
