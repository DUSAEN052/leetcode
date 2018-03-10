class Solution {
    public int countPrimeSetBits(int L, int R) {
        int output = 0;
        Set<Integer> primes = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29));
        
        for (int i = L; i <= R; i ++) {
            int count = Integer.bitCount(i);
            
            if (primes.contains(count)) {
                output ++;
            }
            
        }
        
        return output;
    }
}
