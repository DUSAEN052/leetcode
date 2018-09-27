class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def canRob(curr, nums, memo):
            if curr >= len(nums):
                return 0
            if curr in memo:
                return memo[curr]
            take = nums[curr] + canRob(curr + 2, nums, memo)
            skip = canRob(curr + 1, nums, memo)
            memo[curr] = max(take, skip)
            
            return memo[curr]
        
        return canRob(0, nums, {})
