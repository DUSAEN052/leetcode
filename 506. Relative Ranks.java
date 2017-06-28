public class Solution {
    public String[] findRelativeRanks(int[] nums) {
        int[] nums1 = Arrays.copyOf(nums, nums.length);
        String[] sa = new String[nums.length];
        Map<Integer, String> hs = new HashMap<Integer, String>();
        Arrays.sort(nums);
        
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                hs.put(nums[i], "Gold Medal");
            } else if (i == nums.length - 2) {
                hs.put(nums[i], "Silver Medal");
            } else if (i == nums.length - 3) {
                hs.put(nums[i], "Bronze Medal");
            } else {
                hs.put(nums[i], Integer.toString(nums.length - i));
            }
        }
        
        for (int j = 0; j < nums.length; j++) {
            sa[j] = hs.get(nums1[j]);
        }
        
        return sa;
    }
}
