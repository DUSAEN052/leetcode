public class Solution {
    public int maxProfit(int[] prices) {
        int output = 0;
        if (prices.length == 0) {
            return 0;
        }
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < prices[i+1]) {
                output = output + (prices[i+1] - prices[i]);
            }
        }
        return output;
    }
}
