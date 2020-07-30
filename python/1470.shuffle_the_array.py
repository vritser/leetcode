from typing import List

# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs, ys = nums[0:n], nums[n:]
        return [t for ts in list(zip(xs, ys)) for t in ts]

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        xs, ys = nums[0:n], nums[n:]
        return list(sum(list(zip(xs, ys)), ()))
