class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        sortedPeople = sorted(people)
        count, left, right = 0, 0, len(people) - 1
        
        while left <= right:
            if sortedPeople[left] + sortedPeople[right] <= limit:
                left += 1
            right -= 1
            count += 1
        
        return count
