public class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int[][] output = new int[r][c];
        int size = nums.length * nums[0].length;
        int n2 = r * c;
        Queue<Integer> q = new LinkedList<Integer>();

        if (size != n2) {
            return nums;
        }
        
        for (int a = 0; a < nums.length; a++) {
            for (int b = 0; b < nums[0].length; b++) {
                q.add(nums[a][b]);
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                output[i][j] = q.poll();
            }
        }
        
        return output;
    }
}
