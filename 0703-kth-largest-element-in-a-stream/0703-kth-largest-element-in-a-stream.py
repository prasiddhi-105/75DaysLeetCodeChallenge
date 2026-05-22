import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        # Add all initial numbers
        for num in nums:
            self.add(num)

    def add(self, val):

        # Add value into heap
        heapq.heappush(self.heap, val)

        # Keep only k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Top element = kth largest
        return self.heap[0]