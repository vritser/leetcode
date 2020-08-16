from typing import List
import itertools
import operator

# https://leetcode.com/problems/maximum-average-subarray-i
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = list(itertools.accumulate(nums, operator.add))

        res = sum[k - 1]
        for i in range(k, n):
            res = max(res, sum[i] - sum[i - k])

        return res / k;
