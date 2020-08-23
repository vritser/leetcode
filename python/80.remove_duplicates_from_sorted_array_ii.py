from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 1] or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i + 1
