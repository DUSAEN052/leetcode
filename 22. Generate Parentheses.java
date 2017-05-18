public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> output = new ArrayList<>();
        make("", n, 0, 0, output);
        return output;
    }
    
    public void make(String sb, int n, int l, int r, List<String> output) {
        if (r == n) {
            output.add(sb);
            return;
        } else {
            if (r < l) {
                make(sb + ")", n, l, r + 1, output);
            }
            if (l < n) {
                make(sb + "(", n, l + 1, r, output);
            }
        }
    }
}
