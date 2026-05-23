import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # Convert all values into negative
        stones = [-stone for stone in stones]

        # Convert list into heap
        heapq.heapify(stones)

        # Run until one or no stone left
        while len(stones) > 1:

            # Take two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # If they are not equal
            if first != second:

                # Push remaining weight
                heapq.heappush(stones, -(first - second))

        # If one stone left
        if stones:
            return -stones[0]

        return 0