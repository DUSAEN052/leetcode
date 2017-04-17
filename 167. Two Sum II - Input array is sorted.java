public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] output = new int[2];
        int other, index;
        
        for (int i = 0; i < numbers.length; i++) {
            other = target - numbers[i];
            index = Arrays.binarySearch(numbers, i + 1, numbers.length, other);
            if (index > i) {
                output[0] = i + 1;
                output[1] = index + 1;
                return output;
            }
        }
        return output;
    }
}
