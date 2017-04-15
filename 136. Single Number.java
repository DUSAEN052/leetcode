public class Solution {
    public int singleNumber(int[] nums) {
        
        HashMap<Integer, String> hm = new HashMap<Integer, String>();
        Integer output = 0;
        
        for (int i = 0; i < nums.length; i++) {
            
            int num = nums[i];
            
            if (hm.containsKey(num) == false) {
                hm.put(num, "a");
            }
            else {
                hm.remove(num);
            }
        }
        
        for (Integer key : hm.keySet()){
            return key;
        }
        
        return output;
    }
}