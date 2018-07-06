import math

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dist, maxc, maxl, maxr = 0, 0, 0, 0

        for i in range(len(seats)):
            if seats[i] == 0:
                dist += 1
            
            elif seats[i] == 1:
                maxc = max(dist, maxc)
                dist = 0

        maxc = max(dist, maxc)

        for i in range(len(seats)):
            if seats[i] == 1:
                break
            else:
                maxl += 1

        for i in seats[::-1]:
            if i == 0:
                maxr += 1
            else:
                break

        return max(math.ceil(maxc / 2), maxr, maxl)
