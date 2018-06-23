from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        freq = defaultdict(list)
        output = ''
        
        for item in count:
            freq[count[item]].append(item)
        
        freqcount = sorted(list(freq.keys()))[::-1]
        
        for fc in freqcount:
            output += ''.join(f * fc for f in freq[fc])
        
        return output
