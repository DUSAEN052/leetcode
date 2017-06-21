public class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> hs = new HashMap<Integer, Integer>();
        int output = count(n, hs);
        return output;
    }
    
    public int count(int curr, Map<Integer, Integer> hs) {
        int val = 0;
        
        if (hs.containsKey(curr)) {
            return hs.get(curr);
        } else {
            if (curr < 1) {
                val = 0;
            } else if (curr == 2) {
                val = 2;
            } else if (curr == 1) {
                val = 1;
            } else {
                val = count(curr - 1, hs) + count(curr - 2, hs);
            }
            hs.put(curr, val);
        }
        return val;
    }
}
