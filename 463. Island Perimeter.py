class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count += 4
                    
                    if x < len(grid) - 1 and grid[x + 1][y] == 1:
                        count -= 1
                    if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
                        count -= 1
                    if x > 0 and grid[x - 1][y] == 1:
                        count -= 1
                    if y > 0 and grid[x][y - 1] == 1:
                        count -= 1
                
        return count
