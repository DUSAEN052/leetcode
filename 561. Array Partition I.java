public class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int output = 0;
        for (int i = 0; i < nums.length - 1; i+=2) {
            output += Math.min(nums[i], nums[i+1]);
        }
        return output;
    }
}
