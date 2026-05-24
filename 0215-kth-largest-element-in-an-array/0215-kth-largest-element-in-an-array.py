import heapq

class Solution:
    def findKthLargest(self, nums, k):

        heap = []

        for num in nums:

            # Add element
            heapq.heappush(heap, num)

            # Keep only k largest elements
            if len(heap) > k:
                heapq.heappop(heap)

        # Top element = kth largest
        return heap[0]