from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        distances = [float('inf')] * n
        distances[src] = 0

        for i in range(K + 1):
            temp = distances[:]

            for flight in flights:
                temp[flight[1]] = min(temp[flight[1]], distances[flight[0]] + flight[2])

            distances = temp

        if distances[dst] == float('inf'):
            return -1
        else:
            return distances[dst]
