class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (duration == 0 || timeSeries.length == 0) {
            return 0;
        }
        int output = 0;
        int counter = timeSeries[0];
        
        for (int i = 1; i < timeSeries.length; i++) {
            output += Math.min(duration, timeSeries[i] - timeSeries[i - 1]);
        }
        
        return output + duration;
    }
}
