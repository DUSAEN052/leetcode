from collections import Counter
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        freq = {}
        output = ''
        
        for item in count:
            if count[item] in freq:
                freq[count[item]].append(item)
            else:
                freq[count[item]] = [item]
        
        freqcount = sorted(list(freq.keys()))[::-1]
        
        for fc in freqcount:
            output += ''.join(f * fc for f in freq[fc])
        
        return output
