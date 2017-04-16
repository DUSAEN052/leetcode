public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] note = new int[26];
        int[] mag = new int[26];
        for (int i = 0; i < ransomNote.length(); i++) {
            note[ransomNote.charAt(i) - 'a'] += 1;
        }
        for (int j = 0; j < magazine.length(); j++) {
            mag[magazine.charAt(j) - 'a'] += 1;
        }
        for (int k = 0; k < 26; k++) {
            if (note[k] > mag[k]) {
                return false;
            }
        }
        return true;
    }
}
