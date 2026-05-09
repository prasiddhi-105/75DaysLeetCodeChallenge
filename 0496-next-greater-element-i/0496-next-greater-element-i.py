class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        next_greater = {}

        # Find next greater element for nums2
        for num in nums2:

            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        # Remaining elements have no next greater
        while stack:
            next_greater[stack.pop()] = -1

        ans = []

        # Get answers for nums1
        for num in nums1:
            ans.append(next_greater[num])

        return ans