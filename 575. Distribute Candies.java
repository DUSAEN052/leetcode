public class Solution {
    public int distributeCandies(int[] candies) {
        int output = 0;
        int s = (candies.length)/2;
        Arrays.sort(candies);
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int i = 0; i < candies.length; i++) {
            hs.add(candies[i]);
        }
        if (hs.size() > s) {
            return s;
        }
        output = hs.size();
        return output;
    }
}
