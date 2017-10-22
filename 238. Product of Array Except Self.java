class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        output[0] = 1;
        
        for (int i = 1; i < nums.length; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }
        int temp = 1;
        for (int k = nums.length - 1; k >= 0; k--) {
            output[k] = output[k] * temp;
            temp = temp * nums[k];
        }      
        return output;
    }
}
