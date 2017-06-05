public class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int len1 = num1.length() - 1;
        int len2 = num2.length() - 1;
        int carry = 0;
        int sum = 0;
        
        while (len1 >= 0 || len2 >= 0) {
            int one = 0;
            int two = 0;
            
            if (len1 >= 0) {
                one = num1.charAt(len1) - '0';
            } else {
                one = 0;
            }
            if (len2 >= 0) {
                two = num2.charAt(len2) - '0';
            } else {
                two = 0;
            }
            if (sum > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            sum = one + two + carry;
            sb.insert(0, sum%10);
            carry = sum/10;
            len1 --;
            len2 --;
        }
        
        if (carry == 1) {
            sb.insert(0, 1);
        }
        
        return sb.toString();
    }
}
