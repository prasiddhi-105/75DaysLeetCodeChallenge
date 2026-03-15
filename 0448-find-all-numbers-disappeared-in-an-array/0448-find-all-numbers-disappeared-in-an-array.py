class Solution:
    def findDisappearedNumbers(self, nums):
        
        # Step 1: marking the numbers as visited
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: finding the missing numbers
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result