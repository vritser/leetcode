from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j-=1
            else:
                i+=1

        return []
