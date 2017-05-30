public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int output = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        for (int i = 0; output < g.length && i < s.length; i++) {
            if (g[output] <= s[i]) {
                output++;
            }
        }
        return output;
    }
}
