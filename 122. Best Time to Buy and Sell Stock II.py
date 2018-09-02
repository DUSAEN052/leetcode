class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        output = 0
        
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                output += prices[i + 1] - prices[i]
        
        return output
