public class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sa = new int[26];
        int[] ta = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sa[s.charAt(i) - 'a'] += 1;
        }
        for (int j = 0; j < t.length(); j++) {
            ta[t.charAt(j) - 'a'] += 1;
        }
        for (int k = 0; k < 26; k++) {
            if (sa[k] != ta[k]) {
                return false;
            }
        }
        return true;
    }
}
