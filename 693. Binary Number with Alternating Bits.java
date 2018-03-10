class Solution {
    public boolean hasAlternatingBits(int n) {
        boolean output = true;
        String binaryRep = Integer.toBinaryString(n);
        int strLen = binaryRep.length();
        
        for (int i = 0; i < strLen - 1; i++) {
            if (binaryRep.charAt(i) == binaryRep.charAt(i + 1)) {
                return false;
            }
        }
        
        return output;
    }
}
