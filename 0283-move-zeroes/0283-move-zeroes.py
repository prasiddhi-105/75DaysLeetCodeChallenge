class Solution:
    def moveZeroes(self, nums):
        j = 0  # next position for non-zero
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1