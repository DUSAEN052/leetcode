from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.maxheap and not self.minheap:
            heappush(self.maxheap, -num)
        elif num > -self.maxheap[0]:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -num)
        
        if len(self.maxheap) - len(self.minheap) >= 2:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) - len(self.minheap) <= -2:
            heappush(self.maxheap, -heappop(self.minheap))

    
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        else:
            return -self.maxheap[0] / 1.0 if len(self.maxheap) > len(self.minheap) else self.minheap[0] / 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
