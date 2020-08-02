# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        if 0 <= x < 2: return True

        l, r = 0, x
        while l < r:
            m = int((r + l) / 2)
            y = x / m
            if y == m:
                return True
            if (y < m):
                r = m
            else:
                l = m + 1

        return False
