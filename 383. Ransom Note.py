from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magCount = Counter(magazine)

        for letter in ransomNote:
            if letter in magCount:
                if magCount[letter] != 0:
                    magCount[letter] -= 1
                else:
                    return False
            else:
                return False
        return True
