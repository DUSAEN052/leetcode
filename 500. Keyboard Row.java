public class Solution {
    public String[] findWords(String[] words) {
        List<String> ss = new ArrayList<String>();
        int i = 0;
        for (String s : words) {
            if (check(s.toLowerCase())) {
                ss.add(s);
            }
        }
        String[] output = new String[ss.size()];
        for (String a : ss) {
            output[i] = a;
            i += 1;
        }
        return output;
    }
    
    public boolean check(String str) {
        String r1 = "qwertyuiop";
        String r2 = "asdfghjkl";
        String r3 = "zxcvbnm";
        char[] s = str.toCharArray();
        boolean output = true;
        
        for (char c : s) {
            if (r1.indexOf(c) >= 0) {
                output = true;
            } else {
                output = false;
                break;
            }
        }
        if (output == true) {
            return true;
        } else {
            for (char c : s) {
                if (r2.indexOf(c) >= 0) {
                    output = true;
                } else {
                    output = false;
                    break;
                }
            }
            if (output == true) {
                return true;
            } else {
                for (char c : s) {
                    if (r3.indexOf(c) >= 0) {
                        output = true;
                    } else {
                        output = false;
                        break;
                    }
                }
            }
        }
        return output;
    }
}
