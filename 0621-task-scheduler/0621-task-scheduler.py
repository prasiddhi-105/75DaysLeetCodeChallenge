from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):

        # Count frequency of tasks
        freq = Counter(tasks)

        # Maximum frequency
        max_freq = max(freq.values())

        # Count tasks having max frequency
        max_count = 0

        for value in freq.values():
            if value == max_freq:
                max_count += 1

        # Formula
        intervals = (max_freq - 1) * (n + 1) + max_count

        # Answer can never be less than total tasks
        return max(intervals, len(tasks))