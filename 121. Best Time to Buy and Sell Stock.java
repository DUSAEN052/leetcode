public class Solution {
    public int maxProfit(int[] prices) {
        int output = 0;
        int max = 0;
        
        for (int j = prices.length - 1; j >= 0; j--) {
            output = Math.max(output, max - prices[j]);
            max = Math.max(max, prices[j]);
        }
        
        return output;
    }
}
