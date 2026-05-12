# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            # If mid is bad, first bad can be mid or before
            if isBadVersion(mid):
                right = mid

            # If mid is good, first bad is after mid
            else:
                left = mid + 1

        return left