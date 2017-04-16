public class Solution {
    public char findTheDifference(String s, String t) {
        int[] sa = new int[26];
        int[] ta = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sa[s.charAt(i) -'a']+=1;
        }
        for (int k = 0; k < t.length(); k++) {
            ta[t.charAt(k) -'a']+=1;
        }
        for (int j = 0; j < 26; j++) {
            if (sa[j] != ta[j]) {
                return (char)(j+97);
            }
        }
        return 'a';
    }
}
