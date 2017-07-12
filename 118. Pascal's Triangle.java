public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>>  output = new ArrayList<List<Integer>>();
        
        for (int i = 0; i < numRows; i++) { // rows
            List<Integer> row = new ArrayList<Integer>();
            
            for (int j = 0; j < i + 1; j++) { // row slots
                if (j == 0) {
                    row.add(1);
                } else if (j == i && i != 0) {
                    row.add(1);
                } else {
                    row.add(output.get(i - 1).get(j - 1) + output.get(i - 1).get(j));
                }
            }
            output.add(row);
        }
        return output;
    }
}
