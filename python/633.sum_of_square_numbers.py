import math

# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for  a in range(int(c ** 0.5) + 1):
            b = math.sqrt(c - a * a)
            if (b == int(b)):
                return True
        return False
