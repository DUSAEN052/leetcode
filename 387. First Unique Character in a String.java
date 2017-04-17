public class Solution {
    public int firstUniqChar(String s) {
        int[] array = new int[26];
        ArrayList<Integer> single = new ArrayList<Integer>();
        for (int i = 0; i < s.length(); i++) {
            array[s.charAt(i) - 'a'] +=1;
        }
        for (int j = 0; j < 26; j++) {
            if (array[j] == 1) { // check for unique characters
                single.add(s.indexOf((char)(j + 97)));
            }
        }
        if(single.size() == 0) {
            return -1;
        } else {
            Collections.sort(single);
            return single.get(0);
        }
    }
}
