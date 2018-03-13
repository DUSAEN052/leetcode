class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridR = len(grid)
        gridC = len(grid[0])
        
        def findIsland(grid, i, j, r, c):
            size = 0
            dirs = [(1,0), (-1,0),(0,1),(0, -1)]
            if i >= r or j >= c or i < 0 or j < 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                size += 1
                for dir in dirs:
                    size += findIsland(grid, i + dir[0], j + dir[1], r, c)
            return size
        
        maxIsland = 0
        for i in range(0, gridR):
            for j in range(0, gridC): 
                maxIsland = max(maxIsland, findIsland(grid, i, j, gridR, gridC))
        return maxIsland
