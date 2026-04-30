class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)   # Step 1: store all elements
        max_length = 0

        for num in num_set:
            # Step 2: check if it's start of sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                # Step 3: count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    count += 1

                max_length = max(max_length, count)

        return max_length