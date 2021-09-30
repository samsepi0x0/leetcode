# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            m = (i + j) // 2
            if isBadVersion(m):
                j = m - 1
            else:
                i = m + 1
        return i
