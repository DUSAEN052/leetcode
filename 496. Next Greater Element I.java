public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        int[] output = new int[findNums.length];
        Integer[] num = new Integer[nums.length];
        for (int j = 0; j < nums.length; j++) {
            num[j] = Integer.valueOf(nums[j]);
        }
        for (int i = 0; i < findNums.length; i++) {
            int index = Arrays.asList(num).indexOf(findNums[i]);
            if (index == nums.length - 1) {
                output[i] = -1;
            } else {
                index += 1;
                while (nums[index] <= findNums[i]) {
                    index += 1;
                    if (index == nums.length) {
                        output[i] = -1;
                        index = Arrays.asList(num).indexOf(findNums[i]);
                        break;
                    }
                }
                if (nums[index] > findNums[i]) {
                  output[i] = nums[index]; 
                }
            }
        }
        return output;
    }
}
