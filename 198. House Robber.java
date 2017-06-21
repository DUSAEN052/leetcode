public class Solution {
    public int rob(int[] nums) {
        int output = 0;
        Map<Integer, Integer> hm = new HashMap<Integer, Integer>();
        if(nums.length == 0) {
            return 0;
        }
        output = house(nums, 0, hm);
        
        return output;
    }
    
    public int house(int[] nums, int index, Map<Integer, Integer> hm) {
        int sum = 0;
        if (index >= nums.length) {
            return sum;
        }
        
        if (hm.containsKey(index)) {
            return hm.get(index);
        } else {
            sum = nums[index];
            int l = sum + house(nums, index + 2, hm);
            int r = house(nums, index + 1, hm);
            sum = Math.max(l,r); 
            hm.put(index, sum);
        }
        
        return sum;
    }
}
