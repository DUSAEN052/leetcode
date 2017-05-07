public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        List<Integer> output = new ArrayList<Integer>();
        List<Integer> a = new ArrayList<Integer>();
        int max = 0;
        int count = k;
        for (int i = 0; i < nums.length; i++) {
            if (hm.containsKey(nums[i]) == false) {
                hm.put(nums[i], 1);
            } else {
                hm.put(nums[i], hm.get(nums[i]) + 1);
            }
        }
        for (Integer i : hm.values()) {
            a.add(i);
        }
        Collections.sort(a);
        System.out.println(a);
        while (count != 0) {
            for (Map.Entry<Integer, Integer> entry : hm.entrySet()) {
                Integer key = entry.getKey();
                Integer val = entry.getValue();
                if (val == a.get(a.size()-1)) {
                    output.add(key);
                    count--;
                    hm.remove(key);
                    a.remove(a.size()-1);
                    break;
                }
            }
            
        }
        return output;
    }
}
