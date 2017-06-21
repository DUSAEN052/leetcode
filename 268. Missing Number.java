public class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int output = 0;
        
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] != (nums[i + 1] - 1)) {
                output = (nums[i] + 1);
                return output;
            }
        }
        
        if (nums[0] == 0) {
            return (nums[nums.length - 1]) + 1;
        }
        return nums.length - nums[nums.length - 1];
    }
}
