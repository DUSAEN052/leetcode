class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        
        for (int i = 1; i < matrix.length; i++) {
            for (int k = 1; k < matrix[0].length; k++) {
                    if (matrix[i][k] != matrix[i - 1][k - 1]) {
                        return false;
                    }
                }
            }
        return true;
    }
}
