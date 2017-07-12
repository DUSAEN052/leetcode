public class Solution {
    public int[] constructRectangle(int area) {
        int[] output = new int[2];
        int sq = (int)Math.sqrt(area);
        
        while (area % sq != 0) {
            sq--;
        }
        
        int sq2 = area / sq;
        output[0] = sq2;
        output[1] = sq;
        
        return output;
    }
}
