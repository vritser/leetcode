# https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    def guessNumber(self, n: int) -> int:
        l , r = 1, n

        while l <= r:
            m = int((l + r) / 2)
            cmp = guess(m)

            if cmp == 0:
                return m
            elif cmp == 1:
                l = m + 1
            else:
                r = m - 1
        return -1


def guess(num: int) -> int:
    return 0
