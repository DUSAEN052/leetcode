class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        coins = n
        row = 1
        
        while coins >= row:
            coins -= row
            row += 1
            count += 1
        
        return count
