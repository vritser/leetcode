from typing import List

# https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while l < h:
            m = (l + h) / 2
            if nums[m] == target: return m
            elif nums[m] > target:
                h = m
            else:
                l = m + 1

        return l
