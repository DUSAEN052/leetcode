public class Solution {
    public int islandPerimeter(int[][] grid) {
        int perim = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    perim+=4;
                    
                    if (i != 0 && grid[i-1][j] == 1) { // north
                        perim-=1;
                    }
                    
                    if (i != grid.length-1 && grid[i+1][j] == 1) { // south
                        perim-=1;
                    }
                    
                    if (j != 0 && grid[i][j-1] == 1) { // west
                        perim-=1;
                    }
                    
                    if (j != grid[0].length-1 && grid[i][j+1] == 1) { // east
                        perim-=1;
                    }
                    
                }
            }
        }
        
        return perim;
    }
}