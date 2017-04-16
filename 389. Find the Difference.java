public class Solution {
    public char findTheDifference(String s, String t) {
        int[] sa = new int[26];
        int[] ta = new int[26];
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'a':
                    sa[0]+=1;
                case 'b':
                    sa[1]+=1;
                case 'c':
                    sa[2]+=1;
                case 'd':
                    sa[3]+=1;
                case 'e':
                    sa[4]+=1;
                case 'f':
                    sa[5]+=1;
                case 'g':
                    sa[6]+=1;
                case 'h':
                    sa[7]+=1;
                case 'i':
                    sa[8]+=1;
                case 'j':
                    sa[9]+=1;
                case 'k':
                    sa[10]+=1;
                case 'l':
                    sa[11]+=1;
                case 'm':
                    sa[12]+=1;
                case 'n':
                    sa[13]+=1;
                case 'o':
                    sa[14]+=1;
                case 'p':
                    sa[15]+=1;
                case 'q':
                    sa[16]+=1;
                case 'r':
                    sa[17]+=1;
                case 's':
                    sa[18]+=1;
                case 't':
                    sa[19]+=1;
                case 'u':
                    sa[20]+=1;
                case 'v':
                    sa[21]+=1;
                case 'w':
                    sa[22]+=1;
                case 'x':
                    sa[23]+=1;
                case 'y':
                    sa[24]+=1;
                case 'z':
                    sa[25]+=1;
            }
        }
        for (int k = 0; k < t.length(); k++) {
            switch (t.charAt(k)) {
                case 'a':
                    ta[0]+=1;
                case 'b':
                    ta[1]+=1;
                case 'c':
                    ta[2]+=1;
                case 'd':
                    ta[3]+=1;
                case 'e':
                    ta[4]+=1;
                case 'f':
                    ta[5]+=1;
                case 'g':
                    ta[6]+=1;
                case 'h':
                    ta[7]+=1;
                case 'i':
                    ta[8]+=1;
                case 'j':
                    ta[9]+=1;
                case 'k':
                    ta[10]+=1;
                case 'l':
                    ta[11]+=1;
                case 'm':
                    ta[12]+=1;
                case 'n':
                    ta[13]+=1;
                case 'o':
                    ta[14]+=1;
                case 'p':
                    ta[15]+=1;
                case 'q':
                    ta[16]+=1;
                case 'r':
                    ta[17]+=1;
                case 's':
                    ta[18]+=1;
                case 't':
                    ta[19]+=1;
                case 'u':
                    ta[20]+=1;
                case 'v':
                    ta[21]+=1;
                case 'w':
                    ta[22]+=1;
                case 'x':
                    ta[23]+=1;
                case 'y':
                    ta[24]+=1;
                case 'z':
                    ta[25]+=1;
            }
        }
        for (int j = 0; j < 26; j++) {
            if (sa[j] != ta[j]) {
                return (char)(j+97);
            }
        }
        return 'a';
    }
}
