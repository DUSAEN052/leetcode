class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letters = {}
        checked = set()
        output = []
        count = 0
        
        for letter in S:
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
        
        for letter in S:
            checked.add(letter)
            
            if letters[letter] > 0 and checked:
                count += 1
                letters[letter] = letters[letter] - 1
                
                if letters[letter] == 0:
                    checked.remove(letter)
                    
                    if not checked:
                        output.append(count)
                        count = 0
        
        return output
