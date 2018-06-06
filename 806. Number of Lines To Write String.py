from collections import Counter
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count , line = 0, 1
        
        for letter in S:
            letter_width = widths[ord(letter) - ord('a')]
            
            if count + letter_width > 100:
                line += 1
                count = letter_width
            else:
                count += letter_width
        
        return [line, count]
