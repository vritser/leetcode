from collections import deque
from typing import List

# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()             # Store max k elements
        ans = []

        for i, v in enumerate(nums):
            # Clear all elements less than v
            while q and v > nums[q[-1]]:
                q.pop()

            q.append(i)

            # Outside of the window size k
            if q[0] == i - k:
                q.popleft()

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
