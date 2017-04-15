public class Solution {
    public String reverseString(String s) {
        String rs = "";
        for ( int i = 0; i < s.length(); i++) {
            rs = rs + s.charAt(s.length()-i-1);
        }
        return rs;
    }
}