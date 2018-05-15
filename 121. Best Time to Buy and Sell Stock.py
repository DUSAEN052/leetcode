class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        profit = 0
        minval = prices[0]
        
        for i in range(1, len(prices)):
            minval = min(minval, prices[i])
            profit = max(profit, prices[i] - minval)
        
        return profit
