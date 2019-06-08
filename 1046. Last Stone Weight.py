import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap, -abs(x - y))
        
        return -heap[0]
