class Solution {
    public int numJewelsInStones(String J, String S) {
        int output = 0;
        Map<Character, Integer> hashMap = new HashMap<>();
        
        for (int i = 0; i < J.length(); i++) {
            hashMap.put(J.charAt(i), 0);
        }
        
        for (int k = 0; k < S.length(); k++) {
            if (hashMap.containsKey(S.charAt(k))) {
                output ++;
            }
        }
        
        return output;
    }
}
