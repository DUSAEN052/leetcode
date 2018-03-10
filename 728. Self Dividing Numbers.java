class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> output = new ArrayList<>();
        
        for (int i = left; i <= right; i++) {
            boolean canSelf = true;
            int digit = 0;
            int number = i;
            while (number > 0) {
                digit = number % 10;
                if (digit != 0 && i % digit == 0) {
                
                } else {
                    canSelf = false;
                    break;
                }
                number = number / 10;
            }
            if (canSelf == true) {
                output.add(i);
            }
        }
        
        return output;
    }
}
