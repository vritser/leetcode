from typing import List

# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for j in range(k, len(nums)):
            nums[j] = 0

    def moveZeroes2(self, nums: List[int])-> None:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
