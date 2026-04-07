class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Step 1: target found
            if nums[mid] == target:
                return mid

            # Step 2: check which half is sorted
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1