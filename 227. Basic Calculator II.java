class Solution {
    public int calculate(String s) {
        int output = 0;
        int num = 0;
        char sign = '+';
        Stack<Integer> myStack = new Stack<>();       
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) - '0' >= 0 && s.charAt(i) - '0' <= 9) {
                num = num * 10 + s.charAt(i) - '0';
                if ((i < s.length() - 1 && Character.isDigit(s.charAt(i + 1)) == false) || i == s.length() - 1) {
                    if (sign == '+') {
                        myStack.push(num);
                        num = 0;
                    }
                    if (sign == '-') {
                        myStack.push(-num);
                        num = 0;
                    }
                    if (sign == '*') {
                        myStack.push(myStack.pop() * num);
                        num = 0;
                    }
                    if (sign == '/') {
                        myStack.push(myStack.pop() / num);
                        num = 0;
                    }
                } 
            } else {
                if (s.charAt(i) == '+') {
                    sign = '+';
                    //myStack.push(num);
                }
                if (s.charAt(i) == '-') {
                    sign = '-';
                    //myStack.push(-num);
                }
                if (s.charAt(i) == '*') {
                    sign = '*';
                    //myStack.push(myStack.pop() * num);
                }
                if (s.charAt(i) == '/') {
                    sign = '/';
                    //myStack.push(myStack.pop() / num);
                }
                num = 0;
            }
        }
        
        for (int n : myStack) {
            
            output += n;
        }
        
        return output;
    }
}
