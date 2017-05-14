public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> output = new ArrayList<>();
        List<String> base = new ArrayList<>();
        StringBuffer sb = new StringBuffer("");
        make("", n, 0, 0, output);
        return output;
    }
    
    public void make(String sb, int n, int l, int r, List<String> output) {
        if (r == n) {
            output.add(sb);
            return;
        } else {
            if (r < l) {
                //sb += ")";
                //System.out.println(sb);
                make(sb + ")", n, l, r + 1, output);
            }
            if (l < n) {
                //sb += "(";
                //System.out.println(sb);
                make(sb + "(", n, l + 1, r, output);
            }
        }
    }
}
