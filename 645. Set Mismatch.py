from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counted = Counter(nums)
        output = [num for num, count in counted.items() if count == 2]
        
        for i in range(1, len(nums) + 1):
            if i not in counted:
                output.append(i)
                return output
