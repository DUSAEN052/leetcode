class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_bottom = {} # max of each column
        left_right = {} # max of each row
        output = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j in top_bottom:
                    top_bottom[j] = max(top_bottom[j], grid[i][j])
                elif j not in top_bottom:
                    top_bottom[j] = grid[i][j]
                if i in left_right:
                    left_right[i] = max(left_right[i], grid[i][j])
                elif i not in left_right:
                    left_right[i] = grid[i][j]
        
        for h in range(len(grid)):
            for k in range(len(grid[0])):
                output += min(top_bottom[k], left_right[h]) - grid[h][k]
        
        return output
