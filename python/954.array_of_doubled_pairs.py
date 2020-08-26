from typing import List
from collections import Counter

# https://leetcode.com/problems/array-of-doubled-pairs/
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2 * x] == 0: return False

            count[x] -= 1
            count[2*x] -= 1

        return True
