# https://leetcode.com/problems/powx-n/
class Solution:
    # if n is even: x^n = (x ^ 2) ^ (n / 2)
    # if n is odd: x ^ n = x * (x ^ 2) ^  (n // 2) or x * (x ^ 2) ^ ((n - 1) / 2)
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        if n % 2  == 0:
            return (x * x) ** (n / 2)
        else:
            return x * (x * x) ** (n // 2)

        def myPow2(self, x: float, n: int) -> float:
            if n == 0: return 1

            if n % 2  == 0: return self.myPow2(x * x, n / 2)
            if n > 0: return x * self.myPow2(x, n - 1)

            return self.myPow2(x, n + 1) / x
