public class Solution {
    
    class Position {
        int row;
        int col;
        Position(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    
    public List<List<String>> solveNQueens(int n) {
       char[][] board = new char[n][n];
       Position[] positions = new Position[n];
       List<List<String>> output = new ArrayList<>();
       check(0, positions, n, output);
       return output;
    }
    
    public void check(int current, Position[] positions, int n, List<List<String>> output) {
        
        if (n == current) { //if no queens left
            List<String> plot = new ArrayList<String>();
            StringBuffer buff = new StringBuffer();
            for (Position p : positions) {
                for (int j = 0; j < n; j++) {
                    if(p.col == j) {
                        buff.append("Q");
                    } else {
                        buff.append(".");
                    }
                }
                plot.add(buff.toString());
                buff = new StringBuffer();
            }
            output.add(plot);
            return;
        }
        
        for (int i = 0; i < n; i++) {
            boolean safe = true;
            
            for (int q = 0; q < current; q++) {
                if(positions[q].col == i || positions[q].row - positions[q].col == current - i || positions[q].row + positions[q].col == i + current) {
                    //check every queen placed for conflict 
                    safe = false;
                    break;
                }
            }
            if (safe) {
                //place queen
                positions[current] = new Position(current, i);
                check(current + 1, positions, n , output);
            }
        }
    }
}
