public class Solution {
    public String reverseVowels(String s) {
        StringBuilder sb = new StringBuilder();
        List<Character> vow = Arrays.asList('a', 'e', 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        int len = s.length();
        Stack stk = new Stack();
        
        for (int i = 0; i < len; i++) {
            if (vow.contains(s.charAt(i))) {
                stk.push(s.charAt(i));
            }
        }
        
        for (int j = 0; j < len; j++) {
            if (vow.contains(s.charAt(j))) {
                sb.append(stk.pop());
            } else {
                sb.append(s.charAt(j));
            }
        }
        
        return sb.toString();
    }
}
