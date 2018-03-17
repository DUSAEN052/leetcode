class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = collections.Counter(nums)
        count = 0
        
        for n in table:
            if n + 1 in table:
                count = max(count, table[n] + table[n + 1])
        
        return count
