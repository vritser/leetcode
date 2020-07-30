from typing import List

# https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0, 0
        ans = []

        for i in range(0, len(nums)):
            print(i, l, r)
            if i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                r += 1
            else:
                if l == r:
                    ans.append(str(nums[r]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))
                l = r = r + 1
        return ans
