from typing import List
from functools import reduce

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return reduce(lambda a, b: (a - 1) * (b - 1), sorted(nums)[-2:])

    def maxProduct2(self, nums: List[int]) -> int:
        fst, snd = 0, 0

        for n in nums:
            if n > fst:
                fst, snd = n, fst
            elif n > snd:
                snd = n

        return (fst - 1) * (snd - 1)
