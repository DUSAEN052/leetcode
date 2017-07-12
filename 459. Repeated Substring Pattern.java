public class Solution {
    public boolean repeatedSubstringPattern(String s) {
        boolean output = false;
        StringBuilder sb = new StringBuilder();
        
        for (int i = 1; i <= s.length() / 2; i++) {
            sb.append(s.substring(0, i));
            
            String myString = sb.toString();
            StringBuilder test = new StringBuilder();
            
            if (s.length() % myString.length() == 0) {
                int mult = s.length() / myString.length();
                
                for (int j = 0; j < mult; j++) {
                    test.append(sb);
                }
                
                if (test.toString().equals(s)) {
                    return true;
                } else {
                    sb = new StringBuilder();
                }
            } else {
                sb = new StringBuilder();
            }
        }
        return output;
    }
}
