public class Solution {
    public boolean isValid(String s) {
        Stack stk = new Stack();
        
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            
            if (a == '(' || a == '[' || a == '{') {
                stk.push(a);
            } else if (!stk.empty()) {
                char b = (char) stk.peek();
                
                if (a == ')' && b == '(') {
                    stk.pop();
                } else if (a == ']' && b == '[') {
                    stk.pop();
                } else if (a == '}' && b == '{') {
                    stk.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return stk.empty();
    }
}
