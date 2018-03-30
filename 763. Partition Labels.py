from collections import Counter

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letters = Counter(S)
        checked = set()
        output = []
        count = 0
        
        for letter in S:
            checked.add(letter)
            
            if letters[letter] > 0 and checked:
                count += 1
                letters[letter] -= 1
                
                if letters[letter] == 0:
                    checked.remove(letter)
                    
                    if not checked:
                        output.append(count)
                        count = 0
        
        return output
