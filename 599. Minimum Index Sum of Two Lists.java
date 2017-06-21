public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        List<Integer> ls = new ArrayList<Integer>();
        HashMap<Integer, List<String>> hs = new HashMap<Integer, List<String>>();
        int sum = 0;
        int min;
        
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    sum = i + j;
                    List<String> as = new ArrayList<String>();
                    
                    if (hs.containsKey(sum) == false) {
                        as.add(list1[i]);
                        hs.put(sum, as);
                    } else {
                        as = hs.get(sum);
                        as.add(list1[i]);
                        hs.put(sum, as);
                    }
                }
            }
        }
        
        for (Integer key : hs.keySet()) {
            ls.add(key);
        }
        
        Collections.sort(ls);
        min = ls.get(0);
        String[] output = hs.get(min).toArray(new String[hs.get(min).size()]);
        
        return output;
    }
}
