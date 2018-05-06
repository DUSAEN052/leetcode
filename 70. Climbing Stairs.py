class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n, curr, memo):
            count = 0
            
            if curr in memo:
                return memo[curr]
            elif curr == n:
                return 1
            elif curr > n:
                return 0
            
            memo[curr] = climb(n, curr + 1, memo) + climb(n, curr + 2, memo)
            
            return memo[curr]
        
        return climb(n, 0, {})
