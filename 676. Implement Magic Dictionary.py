from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = defaultdict(list)
        
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.mapping[len(word)].append(word)
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) in self.mapping:
            for value in self.mapping[len(word)]:
                count = 0
                
                for i in range(len(value)):
                    if value[i] != word[i]:
                        count += 1
                    if count > 1:
                        break
                
                if count == 1:
                    return True
            
            return False
        else:
            return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
