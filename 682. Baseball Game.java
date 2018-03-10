class Solution {
    public int calPoints(String[] ops) {
        int output = 0;
        Stack<Integer> stck = new Stack<>();
        
        for (int i = 0; i < ops.length; i++) {
            if (ops[i].equals("C")) {
                output -= stck.pop();
            } else if (ops[i].equals("D")) {
                int top = stck.peek() * 2;
                output += top;
                stck.push(top);
                
            } else if (ops[i].equals("+")) {
                int top = stck.pop();
                int bottom = stck.peek();
                stck.push(top);
                output += top + bottom;
                stck.push(top + bottom);
            } else {
                output += Integer.parseInt(ops[i]);
                stck.push(Integer.parseInt(ops[i]));
            }
        }
        
        return output;
    }
}
