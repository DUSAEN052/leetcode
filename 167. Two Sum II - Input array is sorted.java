public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] output = new int[2];
        for (int i = 0; i < numbers.length - 1; i++) {
            int j = i + 1;
            while ( j < numbers.length && numbers[i] + numbers[j] != target) {
                j+=1;
            }
            if ( j < numbers.length && numbers[i] + numbers [j] == target) {
                output[0] = i + 1;
                output[1] = j + 1;
            }
        }
        return output;
    }
}
