class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0 for i in range(2)] for i in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(prices[i] + dp[i - 1][1] - fee, dp[i - 1][0])
            dp[i][1] = max(-prices[i] + dp[i - 1][0], dp[i - 1][1])
        
        return dp[-1][0]
