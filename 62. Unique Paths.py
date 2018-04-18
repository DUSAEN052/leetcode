class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1 for i in range(n)] for h in range(m)]
        
        for x in range(1, m):
            for j in range(1, n):
                grid[x][j] = grid[x-1][j] + grid[x][j-1]
        
        return grid[m-1][n-1]
