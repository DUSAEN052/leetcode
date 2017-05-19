public class Solution {
    public int hammingDistance(int x, int y) {
        String x1 = Integer.toString(x, 2);
        String y1 = Integer.toString(y, 2);
        int output = 0;
        int max = Math.max(x1.length(), y1.length());
        String x2 = addZero(x1, max - x1.length());
        String y2 = addZero(y1, max - y1.length());
        
        for (int i = 0; i < max; i++) {
            if(x2.charAt(i) != y2.charAt(i)) {
                output+=1;
            }
        }
        return output;
    }
    
    public String addZero(String x, int y) {
        StringBuilder output = new StringBuilder(x);
        for (int i = 0; i < y; i ++) {
            output.insert(0,'0');
        }
        return output.toString();
    }
}
