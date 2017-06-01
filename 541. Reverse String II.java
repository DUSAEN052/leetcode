public class Solution {
    StringBuilder sb = new StringBuilder();
    public String reverseStr(String s, int k) {
        mod(s, k);
        return sb.toString();
    }
    
    public void mod(String s, int k) {
        int len = s.length();
        int tk = 2 * k;
        int lft = len % tk;
        String sub = "";
        StringBuilder bld = new StringBuilder();
        
        if (len < k) {
            bld.append(s);
            bld.reverse();
            sb.append(bld);
            return;
        } else if (len < tk && len >= k) {
            for (int j = 0; j < k; j++) {
                bld.append(s.charAt(j));
            }
            bld.reverse();
            sb.append(bld);
            sb.append(s.substring(k));
            return;
        } else {
            for (int i = 0; i < k; i++) {
                bld.append(s.charAt(i));
            }
            bld.reverse();
            sb.append(bld);
            sb.append(s.substring(k , tk));
            if (len < tk) {
                return;
            }
            mod(s.substring(tk), k);
        }
    }
}
