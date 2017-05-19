public class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder("");
        String output = "";
        
        for (int i = s.length() - 1; i >= 0; i --){
            sb.append(s.charAt(i));
        }
        String[] str = sb.toString().split("\\s+");
        for (int j = str.length - 1; j >= 0; j--) {
            output = output + str[j] + " ";
        }
        return output.substring(0, output.length() - 1);
    }
}
