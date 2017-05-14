public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        output.add(res);
        Arrays.sort(nums);
        make(nums, 0, res, output);
        return output;
    }
    
    public void make(int[] nums, int start, List<Integer> res, List<List<Integer>> output) {
        for (int i = start; i < nums.length; i++) {
            List<Integer> tmp = new ArrayList<>(res);
            tmp.add(nums[i]);
            output.add(tmp);
            make(nums, i + 1, tmp, output);
        }
    }
}
