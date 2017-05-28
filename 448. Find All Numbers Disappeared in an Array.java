public class Solution {
        public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> output = new ArrayList<Integer>();
        List<Integer> sorted = new ArrayList<Integer>();
        int[] srt = nums;
        int max = 0;
        Arrays.sort(srt);
        for (int i = 0; i < nums.length; i++) {
            sorted.add(srt[i]);
        }
        max = sorted.size();
        if (max == 0) {
            return output;
        }
        if (sorted.get(0) != 1) {
                int dif1 = sorted.get(0) - 1;
                while (dif1 > 0) {
                    output.add(0 + dif1);
                    dif1--;
                }
            }
        
        for (int j = 0; j < max; j++) {
            int curr = sorted.get(j);
            int diff = 0;
            if (j == max - 1) {
                diff = max - sorted.get(max - 1);
                while (diff > 0) {
                    output.add(curr += 1);
                    diff--;
                }
                break;
            }
            int nxt = sorted.get(j + 1);
            int dif = nxt - curr;
            if (dif > 1) {
                while (dif > 1) {
                    output.add(curr += 1);
                    dif--;
                }
            }
        }
        
        return output;
    }
}
