# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n

        while l < r:
            m = int((l + r) / 2)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l
