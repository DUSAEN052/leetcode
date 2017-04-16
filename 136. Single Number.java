public class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> mySet = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (!mySet.contains(nums[i])) {
                mySet.add(nums[i]);
            } else {
                mySet.remove(nums[i]);
            }
        }
        for(Integer num : mySet) {
            return num;
        }
        return 0;
    }
}
