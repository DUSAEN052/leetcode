public class Solution {
    public int findLUSlength(String a, String b) {
        String c = a;
        int output = c.length();
        int a1 = 0;
        int b1 = 0;
        
        if (a.equals(b)) {
            return -1;
        }
        while (output > 0) {
            if (b.contains(c)) {
                a1 = output;
                break;
            } else {
                c = c.substring(0, c.length() - 1);
                System.out.println(c + " a");
            }
        }
        output = 0;
        c = b;
        while (output > 0) {
            if (a.contains(c)) {
                b1 = output;
                break;
            } else {
                c = c.substring(0, c.length() - 1);
                System.out.println(c + " b");
            }
        }
        return Math.max(a.length(), b.length());
    }
}
