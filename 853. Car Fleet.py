class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        fleet = len(position)
        time = {}
        
        for p, s in zip(position, speed):
            time[p] = (target - p) / s
        
        position.sort()
        front = 0
        
        for pos in position[::-1]:
            if front == 0 or time[pos] > front:
                front = time[pos]
            else:
                fleet -= 1

        return fleet
