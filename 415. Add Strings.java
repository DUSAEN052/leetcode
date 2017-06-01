public class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int n1 = 0;
        int n2 = 0;
        int k = 1;
        for (int i = num1.length() - 1; i >= 0; i--) {
            n1 += (num1.charAt(i) - '0') * k;
            System.out.println(n1 + " k " + " i " + i);
            k = k * 10;
        }
        k = 1;
        for (int j = num2.length() - 1; j >= 0; j--) {
            n2 += (num2.charAt(j) - '0') * k;
            k = k * 10;
        }
        System.out.println(n1 +" : " + n2);
        int s = n1 + n2;
        if (s == 0) {
            sb.append('0');
            return sb.toString();
        }
        System.out.println("s : " + s);
        while (s != 0) {
            sb.append(new Integer(s % 10));
            s = s / 10;
        }
        sb.reverse();
        System.out.println("sb : " + sb);
        return sb.toString();
    }
}
