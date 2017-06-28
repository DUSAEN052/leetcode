public class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int si = 0;
        int s0 = Integer.MAX_VALUE;
        int s1 = Integer.MAX_VALUE;
        
        if (ops.length == 0 || ops[0].length == 0) {
            return m * n;
        }
        
        for (int[] a : ops) {
            if (a[0] < m) {
                s0 = Math.min(s0, a[0]);
            }
            if (a[1] < n) {
                s1 = Math.min(s1, a[1]);
            }
        }
        si = s0 * s1;
        
        return si;
    }
}
