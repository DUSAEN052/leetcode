class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        List<Integer> solution = new ArrayList<>();
        Map<Integer, Integer> hm = new HashMap<Integer, Integer>();
        HashSet<List<Integer>> set = new HashSet<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            int target = 0 - nums[i];
            hm.put(target, i);
        }
        
        for (int j = 0; j < nums.length; j++) {
            for (int k = 0; k < nums.length; k++) {
                if (j != k) {
                    int sum = nums[j] + nums[k];
                    if (hm.containsKey(sum) && hm.get(sum) != j && hm.get(sum) !=k && j != k) {
                        solution.add(nums[hm.get(sum)]);
                        solution.add(nums[j]);
                        solution.add(nums[k]);
                        Collections.sort(solution);
                        set.add(solution);
                        solution = new ArrayList<>();
                    } 
                }
                
            }
        }
        
        Iterator<List<Integer>> itr = set.iterator();
        while (itr.hasNext()) {
            output.add(itr.next());
        }
        
        return output;
    }
}
