public class Solution {
    public boolean detectCapitalUse(String word) {
        boolean first = false;
        boolean rest = false;
        
        if (word.toLowerCase().equals(word)) {
            return true;
        } //check if all are lowercase
        
        if (word.toUpperCase().equals(word)) {
            return true;
        } //check if all are uppercase
        
        if (word.charAt(0) >= 'A' && word.charAt(0) <= 'Z') { //if first char is upper mark that down
            first = true;
        }

        for (int i = 1; i < word.length(); i++) { //check if first is upper and if rest are lower
            if (first == true && i > 0) {
                if (word.charAt(i) >= 'a' && word.charAt(i) <= 'z') {
                    rest = true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        
        if (rest == true && first == true) {
            return true;
        }
        
        return true;
    }
}
