public class Solution {
    public char findTheDifference(String s, String t) {
        StringBuffer buff = new StringBuffer(t);
       for (int i = 0; i < s.length(); i++){
           if (t.indexOf(s.charAt(i)) != -1){
               buff.deleteCharAt(buff.indexOf(Character.toString(s.charAt(i))));
           }
       }
       return buff.charAt(0);
    }
}