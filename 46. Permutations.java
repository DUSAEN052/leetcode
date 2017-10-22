class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        List<Integer> myArray = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        find(nums, output, myArray, used);
        return output;
        
    }
    
    public void find(int[] nums, List<List<Integer>> output, List<Integer> input, boolean[] used){
        if (input.size() == nums.length) {
            output.add(new ArrayList<>(input));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] == false) {
                    input.add(nums[i]);
                    used[i] = true;
                    find(nums, output, input, used);
                    input.remove(input.size() - 1);
                    used[i] = false;
                }
            }
        }
    }
}
