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
            if curr == n:
                return 1
            elif curr > n:
                return 0
            
            count += climb(n, curr + 1, memo) + climb(n, curr + 2, memo)
            memo[curr] = count
            
            return count
        
        return climb(n, 0, {})
