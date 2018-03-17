class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cache = {}
        
        def climb(cost, index, cache):
            if index >= len(cost):
                return 0
            elif index in cache:
                return cache[index]
            else:
                cache[index] = cost[index] + min(climb(cost, index + 2, cache), climb(cost, index + 1, cache))
            return cache[index]
        
        return min(climb(cost, 0, cache), climb(cost, 1, cache))
