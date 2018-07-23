class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sortedlist = sorted(people, key=lambda y:y[1])[::-1]
        sortedlistv2 = sorted(sortedlist, key=lambda x:x[0])[::-1]
        output = []
        
        for person in sortedlistv2:
            output.insert(person[1], person)
        
        return output
