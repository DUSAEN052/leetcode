public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        int[] out = new int[0];
        List<Integer> ma = new ArrayList<Integer>();
       
        for (int i = 0; i < nums1.length; i++){
            int s = nums1[i];
            if (!hm.containsKey(s)) {
                hm.put(s, 1);
            } else {
                hm.put(s, hm.get(s) + 1);
            }
        }

        for (int k = 0; k < nums2.length;  k++) {
            int ss = nums2[k];
            if(hm.containsKey(ss)) {
                ma.add(ss);
                hm.put(ss, hm.get(ss) - 1);
                if (hm.get(ss) == 0) {
                    hm.remove(ss);
                }
            }
        }
        
        if (ma.size() == 0) {
            return out;
        }
        
        int[] output = new int[ma.size()];
        
        for (int j = 0; j < ma.size(); j++) {
            output[j] = ma.get(j);
        }

        return output;
    }
}
