public class Solution {
    public int findComplement(int num) {
        String s = Integer.toBinaryString(num);
        int bin = Integer.parseInt(s, 2);
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                sb.append('1');
            } else {
                sb.append('0');
            }
        }
        
        int output = Integer.parseInt(sb.toString(), 2);
        
        return output;
    }
}
