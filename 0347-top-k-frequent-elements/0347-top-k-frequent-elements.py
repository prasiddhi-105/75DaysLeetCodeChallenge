class Solution:
    def topKFrequent(self, nums, k):
        
        freq = {}
        
        # Step 1: counting frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: sorting by frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        
        # Step 3: returning the first k elements
        return sorted_nums[:k]