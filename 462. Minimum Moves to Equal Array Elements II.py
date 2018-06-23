class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortednums = sorted(nums)
        midnum = sortednums[len(sortednums) // 2]
        
        return sum(abs(midnum - num) for num in sortednums)
