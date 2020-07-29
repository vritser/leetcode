from typing import List

# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while l < h:
            m = int((l + h) / 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m
            else:
                l = m + 1

        return -1
