public class Solution {
    public void moveZeroes(int[] nums) {
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) { // find next first 0
                int temp;
                int k = i+1;
                while (k < nums.length && nums[k] == 0) { // find next number thats not 0
                    k+=1;
                }
                if (k == nums.length) {
                    k--;
                }
                temp = nums[k];
                nums[k] = 0;
                nums[i] = temp;
                k = i+1;
            }
        }
    }
}
