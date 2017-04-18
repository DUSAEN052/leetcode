public class Solution {
    public int longestPalindrome(String s) {
        int[] arr = new int[58];
        boolean odd = false;
        boolean single = false;
        int len = 0;
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'A'] += 1;
        }
        for (int j = 0; j < 58; j++) {
            if (arr[j] % 2 == 0) {
                len = len + arr[j];
            } else {
                odd = true;
                len = len + arr[j] - 1;
            }
        }
        
        if (odd) {
            return len + 1;
        }
        
        return len;
    }
}
