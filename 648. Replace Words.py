class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sortedDict = sorted(dict, key=len)
        sent = sentence.split(" ")
        output = ""
        
        for word in sent:
            for sortedWord in sortedDict:
                flag = False
                
                if word.startswith(sortedWord):
                    output += sortedWord
                    flag = True
                    break
            
            if not flag:
                output += word
            
            flag = False
            output += " "
        
        return output.rstrip()
