from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[m] >= target and nums[l] <= target:
                    r = m
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if nums[m] <= target and target <= nums[r]:
                    l = m
                else:
                    r = m - 1

        return -1
