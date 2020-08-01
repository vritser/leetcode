# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        l, r = 0, x
        while l < r:
            m = (r + l) / 2
            # m * m > x, so the square root of x should in l - m
            if (x / m < m):
                r = m
            else:
                l = m + 1

        return l - 1
