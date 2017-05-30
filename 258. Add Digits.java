public class Solution {
    public int addDigits(int num) {
        int output = 0;
        int cpy = num;
        int sum = 0;
        List<Integer> dig = new ArrayList<Integer>();
        
        while (cpy > 0) {
            dig.add(cpy%10);
            cpy = cpy/10;
        }
        for (Integer i : dig) {
            sum += i;
        }
        if (sum > 9) {
            return addDigits(sum);
        }
        return sum;
    }
}
