public class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> hm = new HashMap<Character, Character>();
        
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            char b = t.charAt(i);
            
            if (hm.containsKey(a)) {
                if (hm.get(a) == b) {
                    
                } else {
                    return false;
                }
            } else {
                if (hm.containsValue(b)) {
                    return false;
                } else {
                    hm.put(a,b);
                }
            }
        }
        
        return true;
    }
}
