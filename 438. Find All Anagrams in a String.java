public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> output = new ArrayList<Integer>();
        int[] pa = new int[26];
        int[] sa = new int[26];
        int pLen = p.length();
        boolean bool = true;
        
        for (int i = 0; i < pLen; i++) {
            pa[p.charAt(i) - 'a'] += 1;
        }
        
        for (int j = 0; j < s.length() - pLen + 1; j++) {
            String ss = s.substring(j, j + pLen);
            
            for (int k = 0; k < pLen; k++) {
                sa[ss.charAt(k) - 'a'] += 1;
            }
            for (int z = 0; z < 26; z++) {
                if (sa[z] != pa[z]) {
                    bool = false;
                    break;
                }
            }
            
            if (bool == true) {
                output.add(j);
            }
            
            bool = true;
            sa = new int[26];
        }
        return output;    
    }
}
